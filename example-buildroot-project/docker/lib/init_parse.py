"""Init file parsing"""
import sys
import json
import logging
from typing import List
from lib.config import Config
from lib.json_helper import JSONHelper
from lib.buildroot import Buildroot
from lib.logger import Logger


class InitParse:
    """Init file parsing class."""

    def _parse_env(self):
        environment = {}
        if "environment" in self.env:
            environment = self.env["environment"][0]
        self.exit_after_build = JSONHelper.parse_attr(
            environment, "exit_after_build", bool, True
        )[1]
        self.user = JSONHelper.parse_attr(environment, "user", str, "br-user")[1]
        self.update = JSONHelper.parse_attr(
            environment, "update_buildroot", bool, False
        )[1]
        self.buildroot_dir_name = JSONHelper.parse_attr(
            environment,
            "buildroot_dir_name",
            str,
            "buildroot",
        )[1]
        self.buildroot_path = "/home/{}/buildroot".format(self.user)

    def run(self) -> bool:
        """Run all the steps."""
        self._parse_env()
        config = Config(self.buildroot_path, self.apply_configs)
        if self.update:
            Buildroot.update(self.buildroot_path)
        for defconfig in self.env["configs"]:
            config_obj = config.parse(defconfig)
            if config_obj["skip"]:
                Logger.print_step("Skipping {}".format(config_obj["defconfig"]))
                continue
            if not config.clean():
                return False
            if not config.apply():
                return False
        for defconfig in self.env["configs"]:
            config_obj = config.parse(defconfig)
            if not config_obj["build"] or config_obj["skip"] or self.no_build:
                Logger.print_step("{}: Skip build step".format(config_obj["defconfig"]))
                continue
            if not Buildroot.build(config_obj):
                return False
            if self.clean_after_build:
                config.clean(force=True)
        return True

    def __init__(
        self,
        env_file: str,
        apply_configs: bool,
        no_build: bool,
        clean_after_build: bool,
    ):
        # Prevent older versions of docker from throwing an error.
        with open(env_file) as env_fd:
            try:
                self.env = json.load(env_fd)
            except json.decoder.JSONDecodeError as err:
                logging.error(str(err))
                sys.exit(-1)
        self.apply_configs = apply_configs
        self.user: str = "br-user"
        self.buildroot_path: str = "/home/{}/buildroot".format(self.user)
        self.fragment_dir: str = ""
        self.fragments: List[str] = []
        self.fragments = None
        self.no_build = no_build
        self.clean_after_build = clean_after_build
