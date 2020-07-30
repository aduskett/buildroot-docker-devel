# Overview
This directory contains all necessary directories and files of which to use buildroot for professional products.

## Reasons for using containers to build
Containers provide the following:
  - A consistent build environment
  - Easy setup and onboarding
  - Reproducible builds
  - An all-in-one setup process.

## Directory structure
This directory has the following structure:
  - buildroot
    - A stock buildroot download found at [buildroot.org](https://buildroot.org/) 
  - docker
    - Contains two files:
      - env_file
        - This file contains several environment variables used during the init process.
      - init
        - Automatically set's up the buildroot environment on startup and then runs /bin/bash to keep the docker container running.
  - my_company
    - The my_company directory contains several directories used for persistent storage purposes.
        - board:
          - Board specific files and directories.
        - configs:
          - Buildroot defconfig files. During the initialization process, the docker init script loops through this directory and applies each config to my_company/output.
        - dl:
          - This directory contains all downloaded source packages used in the above configs in a compressed format.
        - output:
          - The init-script applies each config file found in my_company/configs to output/config_name, and then the source code is built in that directory.
        - package:
          - Any external packages not in stock Buildroot go here.
        - production:
          - Once built, production images go here.
  - scripts
    - Various scripts used for development purposes.

## Prerequisites:
- A computer running macOS, Linux, or Windows with WSL2
- Docker
- Python3
- docker-compose
- 10 - 20GB of free space.

## Setup
  - First, set the variables in docker/env to what is appropriate for the build.
    By default, the environment variables automatically apply all config files, and the init script automatically builds the beaglebone_defconfig found in my_company/configs.
  - run `docker-compose build`

## Building
If auto-building:
  - run `docker-compose up`

If manually-building:
  - run `docker-compose up -d && && docker exec -ti example-buildroot-project-build /bin/bash`
  - Then navigate to `/home/br-user/buildroot/` and build manually. If `AUTO_CONFIG` is set to 1
    in docker/env, then there are directories automatically created in `/home/br-user/buildroot/my_company/output`

# Customizations

## Changing the buildroot user name
  - Edit the BUILDROOT_USER variable in the docker/env and docker-compose.yml files.

## Changing the buildroot UID and GID
  - The default UID and GID for the buildroot user is 1000, however you may customize the default by either:
    - modifying the docker-compose.yml file directly.
    - passing the UID and GID directly from the command line. IE: `docker-compose build --build-arg UID=$(id -u $(whoami)) --build-arg GID=$(id -g $(whoami))`

## Changing the buildroot directory name
  - Edit the BUILDROOT_DIR variable in the docker/env and docker-compose.yml files.

## Changing the my_company directory name
  - Move the my_company directory to the name of your choice, IE: new_company
  - Run the following:
    - `for i in $(grep -RIwsl 'my_company' .); do sed s%my_company%new_company%g -i ${i}; done`
    - `sed s%example-buildroot-project-build%new_company%g -i docker-compose.yml`

## Adding patches to buildroot
  - Add a directory to the BUILDROOT_PATCH_DIR argument in the docker-compose.yml file.
    Patches are automatically copied and applied to buildroot when `docker-compose build` is ran.

## Adding additional companies
  - Add additional companies by copying the my_company directory to a new directory and adding the company name to the
    COMPANY_NAMES variable in the docker-compose.yml file nad the docker/env file.
    Both variables are SPACE DELIMITED!

## Updating Buildroot
  - Download the buildroot tarball from https://buildroot.org/download.html and replace buildroot.tar.gz with the downloaded tarball.
  - run `docker-compose build`
  Note: If you have a BUILDROOT_PATCH_DIR defined, watch for failures during the build process to ensure that all patches applied cleanly!

## Further reading
Please check [The Buildroot manual](https://buildroot.org/downloads/manual/manual.html) for more information.
