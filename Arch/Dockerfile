FROM archlinux:latest
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

# Install dependencies
RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm \
  bc \
  bison \
  bzip2 \
  cmake \
  cpio \
  dialog \
  expect \
  file \
  flex \
  gcc \
  git \
  make \
  mc \
  nano \
  patch \
  sudo \
  rsync \
  svn \
  unzip \
  wget \
  which \
  xz

RUN set -e; \
  pacman -S --noconfirm python-pip; \
  pip3 install -U pip --prefix=/usr; \
  pip3 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
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
