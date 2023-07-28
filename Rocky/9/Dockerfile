FROM rockylinux:9
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

# Install dependencies
RUN dnf update -y
RUN dnf install -y \
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
  gcc-c++ \
  git \
  glibc-devel.i686 \
  glibc.i686 \
  libgcc.i686 \
  libstdc++-devel.i686 \
  make \
  mc \
  nano \
  ncurses-devel \
  ncurses-devel.i686 \
  patch \
  perl-Data-Dumper \
  perl-ExtUtils-MakeMaker \
  perl-Thread-Queue \
  python3-pip \
  rsync \
  sudo \
  svn \
  unzip \
  wget \
  which \
  xz \
  zlib.i686;

RUN set -e; \
  pip3 install -U pip --prefix=/usr; \
  pip3 install \
  aiohttp==3.8.4 \
  ijson==3.2.2 \
  nose2==0.13.0 \
  pexpect==4.8.0 \
  requests==2.31.0 \
  spdx_lookup==0.3.3;

RUN set -e; \
  useradd -ms /bin/bash br-user; \
  echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc;

COPY brmake /usr/bin

USER br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
