#!/usr/bin/env bash
# This script will test a package using several different environments.
# Default environments:
# CentOS 7
# Debian 11
# Ubuntu 20.04
# Fedora 38

CWD=$(pwd)

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

parse_args(){
  local o O opts

  o='c:t:'
  O='config:test-pkg-args:'
  opts="$(getopt -o "${o}" -l "${O}" -- "${@}")"
  eval set -- "${opts}"

  while [ ${#} -gt 0 ]; do
    case "${1}" in
    (-c|--config)
        CONFIG="${2}"; shift 2
        ;;
    (-t|--test-pkg-args)
        TEST_PKG_ARGS="${2}"; shift 2
        ;;
    (-e|--rebuild)
      REBUILD="true"; shift 1
      ;;
    (-r|--restart)
      RESTART="true"; shift 1
      ;;
    (--root)
      ROOT="true"; shift 1
      ;;
    (-k|--kill)
      KILL="true"; shift 1
      ;;
    (-s|--stop)
      STOP="true"; shift 1
      ;;
    (--)
        shift; break
        ;;
    esac
  done
}


main(){

  if [[ -z "${1}" ]]; then
    echo "Must provide path to a buildroot source tree."
    exit 1
  fi

  if [[ -z "${2}" ]]; then
    echo "Must provide arguments compatible with test-pkg."
    exit 1
  fi
  if [[ $(check_docker_images "br-centos7") == "false" ]]; then
    build_docker_image "Ubuntu" "20.04"
    run_docker_image "br-ubuntu20.04"
  fi
}

main "${@}"
