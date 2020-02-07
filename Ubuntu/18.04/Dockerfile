FROM ubuntu:bionic
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

# Install dependencies
RUN set -e; \
  apt-get update; \
  apt-get install -y apt-utils locales; \
  rm -rf /var/lib/apt/lists/*; \
  localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN set -e; \
  apt-get update; \
  apt-get install -y \
  bzip2 \
  gcc-8-base \
  g++ \
  tar \
  flex \
  bison \
  wget \
  sudo \
  git \
  cmake \
  make \
  gcc \
  unzip \
  file \
  bc \
  patch \
  ncurses-dev \
  python-pip \
  rsync \
  subversion \
  libc6-i386 \
  lib32z1 \
  expect

RUN useradd -ms /bin/bash br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc
RUN chown -R br-user:br-user /home/br-user

COPY brmake /usr/bin

USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user

CMD ["/bin/bash"]
