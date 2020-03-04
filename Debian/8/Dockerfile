FROM debian:8
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=US/Pacific

RUN set -e; \
  apt-get update; \
  apt-get install -y apt-utils; \
  apt-get upgrade -y; \
  apt-get install -y locales;

RUN set -e; \
  rm -rf /var/lib/apt/lists/*; \
  localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

# Setup tzdata first as to avoid a dialog requesting tzdata setup.
RUN set -e; \
  apt-get update; \
  apt-get install -y tzdata; \
  ln -snf /usr/share/zoneinfo/$TZ /etc/localtime; \
  echo $TZ > /etc/timezone;

# Install dependencies
RUN set -e; \
  apt-get update; \
  apt-get upgrade -y; \
  apt-get install -y \
  bash \
  bc \
  bison \
  bzip2 \
  cmake \
  cpio \
  dialog \
  expect \
  file \
  flex \
  g++ \
  gcc \
  git \
  lib32z1 \
  locales \
  make \
  mc \
  mercurial \
  nano \
  ncurses-dev \
  patch \
  rsync \
  subversion \
  sudo \
  svn \
  tar \
  unzip \
  which \
  wget \
  xz

# 32-bit support.
RUN set -e; \
  apt-get install -y \
  gcc-multilib \
  g++-multilib \
  libc6-i386

# Python2
RUN set -e; \
  apt-get install -y python-pip python-dev;

# Use the deadsnakes PPA for ubuntu 14.04 to install python3.5.
RUN set -e; \
  echo "deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu trusty main" > /etc/apt/sources.list.d/deadsnakes.list; \
  echo "deb-src http://ppa.launchpad.net/deadsnakes/ppa/ubuntu trusty main" >> /etc/apt/sources.list.d/deadsnakes.list; \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys F23C5A6CF475977595C89F51BA6932366A755776; \
  apt-get update; \
  apt-get install -y python3.5 python3.5-dev; \
  rm /usr/bin/python3; \
  ln -s /usr/bin/python3.5 /usr/bin/python3; \
  wget -q -O - https://bootstrap.pypa.io/get-pip.py | python3.5;

RUN set -e; \
  pip2 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2; \
  pip3 install \
  nose2==0.9.2 \
  pexpect==4.8.0;

# Generate Locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen; \
  localedef -i en_US -f UTF-8 en_US.UTF-8; \
  locale-gen en_US.UTF-8;

RUN useradd -ms /bin/bash br-user; \
  echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc; \
  chown -R br-user:br-user /home/br-user;

COPY brmake /usr/bin

USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
