import os
import multiprocessing
from typing import Dict, Union
from lib.logger import Logger


class Buildroot:
    @staticmethod
    def parse_defconfig(
        _property: str, defconfig: str, buildroot_dir: str
    ) -> Union[str, None]:
        """Parse a defconfig for a given value.

        :param str _property: A given property of which to search.
        :param str defconfig: A path to the defconfig of which to search.
        :param buildroot_dir: A path to the buildroot directory.
        :returns: A string if the property is found, otherwise None.
        :rtype: bool
        """
        buff = {}
        with open(defconfig) as _defconfig:
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
        if _property in buff:
            return buff[_property]
        return None

    @staticmethod
    def build(config_obj: Dict[str, Union[str, bool]]) -> bool:
        """Build all configs that have the build attribute set to true in env.json.

        :param Dict[str, Union[str, bool]] config_obj: An instantiated config object from the config class.
        :returns: True on success, False on failure.
        :rtype: bool
        """
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
                cores = int(cores / j_level)
            cmd += " -j{}".format(str(cores))
        if os.system(cmd) != 0:
            print("ERROR: Failed to build {}".format(config_obj["defconfig"]))
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
