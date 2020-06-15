FROM centos:8
LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Everything needed to build Buildroot in a reproducable manner."
ENV COMPANY_NAME=my_company

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
  pip2 install -U pip==20.1.1 --prefix=/usr; \
  pip2 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2; \
  dnf --enablerepo=PowerTools install -y xz-lzma-compat; \
  rm /etc/localtime; \
  ln -s /usr/share/zoneinfo/America/Los_Angeles /etc/localtime;

# Add the br-user user, as buildroot should never be built as root.
RUN set -e; \
  useradd -ms /bin/bash br-user; \
  usermod -aG wheel br-user; \
  echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc; \
  chown -R br-user:br-user /home/br-user; \
  mkdir -p /tmp/patches/buildroot;

COPY --chown=br-user:br-user buildroot/ /home/br-user/buildroot
COPY ${COMPANY_NAME}/patches/buildroot/*.diff /tmp/patches/buildroot/
COPY --chown=br-user:br-user docker/init /init

# Ensure that any patches held in company_name/patches/buildroot are applied.
# This ensures that relevant upstream patches cherry-picked from
# https://patchwork.ozlabs.org/project/buildroot/list/ are applied during the
# docker build process.
WORKDIR /home/br-user/buildroot
RUN set -e; \
  cp utils/brmake /usr/bin/brmake; \
  chmod +x /usr/bin/brmake; \
  for i in /tmp/patches/buildroot/*.diff; do patch -p1 < "${i}"; done; \
  rm -rf /tmp/patches/buildroot/;

# Perform the following:
# - Pre-emtpively create the ccache diretory for permission purposes.
# - Remove the stock configs and board directory from buildroot.
# - Link company_name/{board,configs,dl} to the base buildroot directory.
# These changes bypass the need to modify buildroot, and allows keeping
# company_name specific configs, downloads, and board files in the company_name directory.
RUN set -e; \
  mkdir -p /home/br-user/ccache; \
  chown -R br-user:br-user /home/br-user/ccache; \
  rm -rf configs; \
  rm -rf board; \
  ln -s /mnt/${COMPANY_NAME} ${COMPANY_NAME}; \
  ln -s ${COMPANY_NAME}/board board; \
  ln -s ${COMPANY_NAME}/configs configs; \
  ln -s ${COMPANY_NAME}/dl dl;

USER br-user
ENV HOME /home/br-user
WORKDIR /home/br-user/buildroot

ENTRYPOINT ["/init"]
CMD ["/bin/bash"]

