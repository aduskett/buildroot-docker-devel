#!/usr/bin/env bash
# This script will test a package using several different environments.


# Default environments:
# CentOS 6
# Debian 8 and 10
# Ubuntu 14.04
# Fedora 31

MACOS="false"
function check_environment(){
  if [[ ! -z $(uname -r |grep Darwin) ]]; then
    MACOS="true"
}

function check_docker_images(){
  check=$(docker images -f "reference=${1}")
  if [[ -z ${check} ]]; then
    echo "false"
    return
  fi
  echo "true"
}

function main(){
  check_environment
  

}