FROM debian:9
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

# Install dependencies
RUN set -e; \
  apt-get update; \
  apt-get upgrade -y; \
  apt-get install -y \
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
  locales-all \
  make \
  nano \
  ncurses-dev \
  patch \
  python-pip \
  rsync \
  subversion \
  sudo \
  tar \
  unzip \
  wget

# 32-bit support.
RUN set -e; \
  apt-get install -y \
  gcc-multilib \
  g++-multilib \
  libc6-i386

RUN pip install nose2 pexpect
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen; \
 localedef -i en_US -f UTF-8 en_US.UTF-8; \
 locale-gen en_US.UTF-8; \
 useradd -ms /bin/bash br-user; \
 echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
 echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc; \
 chown -R br-user:br-user /home/br-user;

COPY brmake /usr/bin

USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
