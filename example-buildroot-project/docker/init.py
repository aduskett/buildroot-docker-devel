#!/usr/bin/env python3
import os
import sys
import signal
from typing import List
from lib.init_parse import InitParse


def signal_handler(sig, _):
    """Handle signals.

    :param int sig: The signal of which to handle.
    """
    if sig == signal.SIGINT:
        print("\n## Exiting. ##\n")
        sys.exit(0)


def main():
    cwd = os.getcwd()
    signal.signal(signal.SIGINT, signal_handler)
    apply_configs = bool(os.environ.get("APPLY_CONFIGS", "false").lower() == "true")
    env_files: List[str] = os.environ.get("ENV_FILES", "env.json").split(":")
    no_build = bool(os.environ.get("NO_BUILD", "false").lower() == "true")
    clean_after_build = bool(
        os.environ.get("CLEAN_AFTER_BUILD", "false").lower() == "true"
    )

    if no_build:
        sys.stdout.write("NO_BUILD environment variable set. Skipping build step!\n")
    for i, _ in enumerate(env_files):
        env_files[i] = "/mnt/docker/{}".format(env_files[i].replace('"', ""))
    for env_file in env_files:
        if not os.path.isfile(env_file):
            sys.stderr.write("{}: No such file\n".format(env_file))
            sys.exit(-1)
    if not env_files:
        sys.stderr.write("No environment files defined!\n")
        sys.exit(-1)
    for env_file in env_files:
        init = InitParse(env_file, apply_configs, no_build, clean_after_build)
        if not init.run():
            sys.exit(-1)
        os.chdir(cwd)
    sys.exit(0)


if __name__ == "__main__":
    main()
