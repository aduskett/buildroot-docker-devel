FROM ubuntu:focal
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
  curl \
  dialog \
  expect \
  file \
  flex \
  g++ \
  gcc \
  git \
  lib32z1 \
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
  wget \
  gcc-multilib \
  g++-multilib \
  libc6-i386;

RUN set -e; \
  pip3 install -U pip; \
  pip3 install \
  aiohttp==3.7.3 \
  cve==1.0.1 \
  ijson==3.1.3 \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  requests==2.25.1 \
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
