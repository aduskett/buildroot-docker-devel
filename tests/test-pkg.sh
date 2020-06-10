#!/usr/bin/env bash
# This script will test a package using several different environments.
# Default environments:
# CentOS 6
# Debian 8 and 10
# Ubuntu 14.04
# Fedora 31

CWD=$(pwd)
MACOS="false"

function check_environment(){
  if [[ ! -z $(uname -r |grep Darwin) ]]; then
    MACOS="true"
  fi
}

function check_running_container(){
  check=$(docker container ps -aq -f "name=${1}")
  if [[ ! -z ${check} ]]; then
    docker kill ${check}
    docker rm ${check}
  fi
}
function check_docker_images(){
  check=$(docker images -qf "reference=${1}")
  if [[ -z ${check} ]]; then
    echo "false"
    return
  fi
  echo "true"
}

function build_docker_image(){
  cd ${CWD}/../${1}/${2}
  docker-compose build
}

function run_docker_image(){
  cd ${1}
  check_running_container "${2}"
}


function main(){
  check_environment

  if [[ -z "${1}" ]]; then
    echo "Must provide path to a buildroot source tree."
    exit 1
  fi

  if [[ -z "${2}" ]]; then
    echo "Must provide arguments compatible with test-pkg."
    exit 1
  fi
  if [[ $(check_docker_images "br-centos6") == "false" ]]; then
    build_docker_image "Ubuntu" "19.10"
    run_docker_image "br-ubuntu19.10"
  fi
}

main "${@}"
