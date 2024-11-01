FROM ubuntu:bionic
LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=US/Pacific

RUN set -e; \
  apt --allow-unauthenticated update; \
  apt --allow-unauthenticated upgrade -y; \
  apt-get install -y apt-utils locales tzdata; \
  localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8; \
  locale-gen en_US.UTF-8; \
  ln -snf /usr/share/zoneinfo/$TZ /etc/localtime; \
  echo $TZ > /etc/timezone;


# We need at least GCC 10 on the host.
RUN set -e; \
  apt-get install -y software-properties-common; \
  add-apt-repository ppa:savoury1/gcc-defaults-10; \
  apt-get update; \
  apt-get upgrade -y; \
  apt-get dist-upgrade -y

# Install dependencies
RUN set -e; \
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
  gcc-multilib \
  git \
  g++-multilib \
  lib32z1 \
  libc6-i386 \
  make \
  mc \
  mercurial \
  nano \
  ncurses-dev \
  patch \
  python3-dev \
  python3-pip \
  rsync \
  subversion \
  sudo \
  tar \
  unzip \
  wget;

# Python3 is needed for support/testing/run-tests
RUN set -e; \
  python3 -m pip install -U pip; \
  python3 -m pip install --force \
  aiohttp==3.8.4 \
  ijson==3.2.2 \
  nose2==0.13.0 \
  pexpect==4.8.0 \
  requests==2.27.1 \
  spdx_lookup==0.3.3;


RUN useradd -ms /bin/bash br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc
RUN chown -R br-user:br-user /home/br-user

COPY brmake /usr/bin

USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user

CMD ["/bin/bash"]
