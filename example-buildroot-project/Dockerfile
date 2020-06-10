FROM centos:8
MAINTAINER Adam Duskett <aduskett@gnauk.com>
LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Everything needed to build Buildroot in a reproducable manner."
ENV COMPANY_NAME=my_company


RUN set -e; \
  useradd -ms /bin/bash br-user; \
  usermod -aG wheel br-user; \
  echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc; \
  chown -R br-user:br-user /home/br-user; \
  mkdir -p /tmp/patches;

COPY --chown=br-user:br-user buildroot/ /home/br-user/buildroot
COPY ${COMPANY_NAME}/patches/buildroot/*.diff /tmp/patches/

# Install dependencies
RUN dnf update -y; \
  dnf install -y epel-release; \
  dnf install -y \
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
  gcc \
  gcc-c++ \
  git \
  libstdc++-devel \
  make \
  mc \
  nano \
  ncurses-devel \
  patch \
  perl-Data-Dumper \
  perl-ExtUtils-MakeMaker \
  perl-Thread-Queue \
  rsync \
  sudo \
  svn \
  tar \
  unzip \
  vim \
  wget \
  which \
  xz \
  glibc-devel.i686 \
  libgcc.i686 \
  libstdc++-devel.i686 \
  ncurses-devel.i686 \
  zlib.i686 \
  glibc.i686 \
  python2-pip python3-pip; \
  pip2 install -U pip --prefix=/usr; \
  pip2 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2; \
  dnf --enablerepo=PowerTools install -y xz-lzma-compat; \
  rm /etc/localtime; \
  ln -s /usr/share/zoneinfo/America/Los_Angeles /etc/localtime;

RUN set -e; \
  cd /home/br-user/buildroot/; \
  cp utils/brmake /usr/bin/brmake; \
  chmod +x /usr/bin/brmake; \
  for i in $(ls /tmp/patches/*); do patch -p1 < ${i}; done; \
  mkdir -p output; \
  chown -R br-user:br-user output;

USER br-user
RUN set -e; \
  cd /home/br-user/buildroot/; \
  rm -rf configs; \
  rm -rf board; \
  ln -s /mnt/${COMPANY_NAME} ${COMPANY_NAME}; \
  ln -s ${COMPANY_NAME}/board board; \
  ln -s ${COMPANY_NAME}/configs configs; \
  ln -s ${COMPANY_NAME}/dl dl;

ENV HOME /home/br-user
WORKDIR /home/br-user/buildroot

COPY --chown=br-user:br-user docker/init /init

ENTRYPOINT ["/init"]
CMD ["/bin/bash"]

