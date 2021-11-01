import os
import multiprocessing
from shutil import rmtree
from typing import Dict, Union
from lib.logger import Logger
from lib.files import Files


class Buildroot:
    @staticmethod
    def parse_defconfig(
        defconfig_property: str, defconfig: str, buildroot_dir: str
    ) -> Union[str, None]:
        """Parse a defconfig for a given value.

        :param str defconfig_property: A given property of which to search.
        :param str defconfig: A path to the defconfig of which to search.
        :param buildroot_dir: A path to the buildroot directory.
        :returns: A string if the property is found, otherwise None.
        :rtype: bool
        """
        buff = {}
        with open(defconfig, encoding="utf-8") as _defconfig:
            for line in _defconfig:
                try:
                    line = line.strip()
                    if "is not set" in line:
                        continue
                    key_val = line.split("=")
                    key = key_val[0]
                    val = key_val[1]
                    buff[key] = val.replace('"', "").replace("$(TOPDIR)", buildroot_dir)
                except IndexError:
                    continue
        _defconfig.close()
        if defconfig_property in buff:
            return buff[defconfig_property]
        return None

    @staticmethod
    def legal_info(config_obj: Dict[str, Union[str, bool]]) -> bool:
        """Generate legal documentation."""
        cmd = "{} BR2_DL_DIR={} legal-info".format(
            config_obj["make"], config_obj["dl_dir"]
        )
        board_name = config_obj["defconfig"].replace("_defconfig", "")
        legal_info_tarball = "{}-legal-info.tar.gz".format(board_name)
        legal_info_path = "{}/legal-info".format(config_obj["build_path"])
        os.chdir(config_obj["build_path"])
        if Files.exists(
            "{}/images/{}-legal-info.tar.gz".format(
                config_obj["build_path"], board_name
            )
        ):
            Logger.print_step("Legal info already generated.")
            return True
        Logger.print_step(
            "Generating legal-info for {}".format(config_obj["defconfig"])
        )
        if os.system(cmd):
            print(
                "ERROR: Failed to generate legal information for {}".format(
                    config_obj["defconfig"]
                )
            )
            if config_obj["make"] == "brmake":
                log = Files.to_buffer(
                    "{}/br.log".format(config_obj["build_path"]), split=True
                )
                for line in log[-100:]:
                    print(line)
            return False
        # We dont want the sources bundled in the tarball.
        rmtree("{}/sources".format(legal_info_path))
        rmtree("{}/host-sources".format(legal_info_path))
        if os.system("tar -czf {} legal-info".format(legal_info_tarball)):
            return False
        if os.makedirs("images", exist_ok=True):
            return False
        if os.system("mv {} images/".format(legal_info_tarball)):
            return False
        return True

    @staticmethod
    def build(config_obj: Dict[str, Union[str, bool]]) -> bool:
        """Build all configs that have the build attribute set to true in env.json.

        :param Dict[str, Union[str, bool]] config_obj: An instantiated config object from the
                                                       config class.
        :returns: True on success, False on failure.
        :rtype: bool
        """
        build_package = os.environ.get("BUILD_PACKAGE", None)
        os.chdir(config_obj["build_path"])
        Logger.print_step("Building {}".format(config_obj["defconfig"]))
        cmd = "{} BR2_DL_DIR={}".format(config_obj["make"], config_obj["dl_dir"])
        # Check if per_package directories is set. If so, check if BR2_JLEVEL is set and divide
        # by the number of cores by JLEVEL.
        if config_obj["per_package"]:
            cores = multiprocessing.cpu_count()
            j_level = int(
                Buildroot.parse_defconfig(
                    "BR2_JLEVEL",
                    "{}/.config".format(config_obj["build_path"]),
                    config_obj["buildroot_path"],
                )
            )
            if j_level:
                cores = max(int(cores / j_level), 1)
            cmd += " -Otarget -j{}".format(str(cores))
            if build_package:
                cmd += " {}".format(build_package)

        if os.system(cmd):
            print("ERROR: Failed to build {}".format(config_obj["defconfig"]))
            if config_obj["make"] == "brmake":
                log = Files.to_buffer(
                    "{}/br.log".format(config_obj["build_path"]), split=True
                )
                for line in log[-100:]:
                    print(line)
            return False
        return True

    @staticmethod
    def update(buildroot_dir: str) -> bool:
        """Update buildroot if it's a git repository.

        :param
        """
        os.chdir(buildroot_dir)
        if not os.path.isdir(".git"):
            print("Buildroot is not from git, skipping update.")
            return True
        retval = os.system("git pull")
        if not retval:
            return False
        return True
