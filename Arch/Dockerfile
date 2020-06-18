FROM archlinux:latest
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

# Install dependencies
RUN pacman -Syu --noconfirm \
  base-devel \
  bc \
  bzip2 \
  cmake \
  cpio \
  dialog \
  expect \
  git \
  mc \
  nano \
  python-nose2 \
  python-pexpect \
  python-pip \
  rsync \
  svn \
  unzip \
  wget \
  xz

RUN set -e; \
  pip3 install -U pip --prefix=/usr; \
  pip3 install \
  spdx_lookup==0.3.2;

RUN set -e; \
  useradd -ms /bin/bash br-user; \
  echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc;

RUN set -e; \
  chown -R br-user:br-user /home/br-user; \
  echo "alias ls='ls --color=auto'" >> /root/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /root/.bashrc

COPY brmake /usr/bin

USER br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8
