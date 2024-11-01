FROM ubuntu:22.04

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=US/Pacific

RUN set -e; \
  mkdir -p /data/; \
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
  apt \
  bash \
  bc \
  bison \
  build-essential \
  bzip2 \
  ccache \
  chrpath \
  cmake \
  cpio \
  curl \
  debianutils \
  dialog \
  diffstat \
  expect \
  file \
  flex \
  g++ \
  gawk \
  gcc \
  gcc-multilib \
  git \
  g++-multilib \
  iputils-ping \
  lib32z1 \
  libacl1 \
  libc6-i386 \
  liblz4-tool \
  libsdl2-dev \
  locales \
  make \
  mc \
  mercurial \
  nano \
  ncurses-dev \
  patch \
  pigz \
  python3 \
  python3-dev \
  python3-aiohttp \
  python3-cvelib \
  python3-git \
  python3-ijson \
  python3-jinja2 \
  python3-nose2 \
  python3-pexpect \
  python3-pip \
  python3-requests \
  python3-subunit \
  rsync \
  socat \
  subversion \
  sudo \
  tar \
  texinfo \
  unzip \
  wget \
  xz-utils \
  zip \
  zstd ;

RUN set -e; \
  pip3 install -U pip; \
  pip3 install --force --break-system-packages \
  spdx_lookup==0.3.3;

RUN useradd -ms /bin/bash br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc
RUN chown -R br-user:br-user /home/br-user

COPY brmake /usr/bin
COPY repo /usr/bin
COPY repo_launcher /usr/bin
USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user

CMD ["/bin/bash"]
