FROM ubuntu:eoan
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

RUN set -e; \
  apt-get update; \
  apt-get install -y apt-utils locales; \
  rm -rf /var/lib/apt/lists/*; \
  localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Setup tzdata first as to avoid a dialog requesting tzdata setup.
RUN set -e; \
  apt-get update; \
  apt-get install -y tzdata;

# Install dependencies
RUN set -e; \
  apt-get update; \
  apt-get upgrade -y; \
  apt-get install -y \
  flex \
  bison \
  wget \
  bzip2 \
  sudo \
  git \
  cmake \
  make \
  gcc \
  g++ \
  unzip \
  file \
  bc \
  nano \
  patch \
  ncurses-dev \
  cpio \
  python-pip \
  rsync \
  subversion \
  libc6-i386 \
  lib32z1 \
  mc \
  expect

RUN pip install nose2 pexpect
RUN useradd -ms /bin/bash br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc
RUN chown -R br-user:br-user /home/br-user

COPY brmake /usr/bin

USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user

CMD ["/bin/bash"]
