FROM centos:8
LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Everything needed to build Buildroot in a reproducable manner."

# Install dependencies
RUN dnf update -y; \
  dnf install -y epel-release; \
  dnf install -y dnf-plugins-core; \
  dnf config-manager --set-enabled PowerTools;

RUN set -e; \
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
  glibc-devel.i686 \
  glibc.i686 \
  help2man \
  libatomic \
  libgcc.i686 \
  libstdc++-devel \
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
  rsync \
  sudo \
  svn \
  tar \
  texinfo \
  unzip \
  vim \
  wget \
  which \
  xz \
  xz-lzma-compat \
  zlib.i686 \
  python2-pip python3-pip; \
  pip2 install -U pip==20.2 --prefix=/usr; \
  pip2 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2; \
  rm /etc/localtime; \
  ln -s /usr/share/zoneinfo/America/Los_Angeles /etc/localtime;

# Set these arguments in the docker-compose.yml file and the docker/env file
# if you wish to change the default values.
# Default values:
# BUILDROOT_USER: br-user
# BUILDROOT_DIR: buildroot
# The buildroot source code is extracted to /home/${BUILDROOT_USER}/{BUILDROOT_DIR}
ARG BUILDROOT_USER
ARG BUILDROOT_DIR
ARG BUILDROOT_PATCH_DIR
ARG UID
ARG GID
# Add the ${BUILDROOT_USER} user, as buildroot should never be built as root.
RUN set -e; \
  groupadd -r -g ${GID} ${BUILDROOT_USER}; \
  useradd -ms /bin/bash -u ${UID} -g ${GID} ${BUILDROOT_USER}; \
  usermod -aG wheel ${BUILDROOT_USER}; \
  echo "alias ls='ls --color=auto'" >> /home/${BUILDROOT_USER}/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/${BUILDROOT_USER}/.bashrc; \
  chown -R ${BUILDROOT_USER}:${BUILDROOT_USER} /home/${BUILDROOT_USER};

COPY --chown=${BUILDROOT_USER}:${BUILDROOT_USER} buildroot.tar.gz/ /home/${BUILDROOT_USER}/

RUN set -e; \
  mkdir -p /home/${BUILDROOT_USER}/${BUILDROOT_DIR}; \
  tar -zxf /home/${BUILDROOT_USER}/buildroot.tar.gz --strip-components=1 -C /home/${BUILDROOT_USER}/${BUILDROOT_DIR}; \
  chown -R ${BUILDROOT_USER}:${BUILDROOT_USER} /home/${BUILDROOT_USER}/${BUILDROOT_DIR}; \
  rm -rf /home/${BUILDROOT_USER}/buildroot.tar.gz;

# Copy brmake to /usr/bin for non-verbose builds.
WORKDIR /home/${BUILDROOT_USER}/${BUILDROOT_DIR}
RUN set -e; \
  cp utils/brmake /usr/bin/brmake; \
  chmod +x /usr/bin/brmake;

# Perform the following:
# - Pre-emtpively create the ccache diretory for permission purposes.
# - Link company_name/{board,configs,dl} to the base buildroot directory.
ARG COMPANY_NAMES
RUN set -e; \
  mkdir -p /home/${BUILDROOT_USER}/ccache; \
  chown -R ${BUILDROOT_USER}:${BUILDROOT_USER} /home/${BUILDROOT_USER}/ccache; \
  mkdir -p /tmp/patches; \
  for COMPANY_NAME in ${COMPANY_NAMES}; do \
    ln -s /mnt/${COMPANY_NAME} ${COMPANY_NAME}; \
  done;

# Ensure that any patches held in company_name/patches/buildroot are applied.
# This ensures that relevant upstream patches cherry-picked from
# https://patchwork.ozlabs.org/project/buildroot/list/ are applied during the
# docker build process.

COPY ${BUILDROOT_PATCH_DIR}* /tmp/patches/
RUN set -e; \
  cd  /home/${BUILDROOT_USER}/${BUILDROOT_DIR}; \
  if [ -n "${BUILDROOT_PATCH_DIR}" ]; then \
    for i in $(find /tmp/patches/ -name "*.patch" -exec readlink -f {} \; ); do patch -p1 < "${i}"; done; \
  fi; \
  rm -rf ${BUILDROOT_PATCH_DIR};

COPY --chown=${BUILDROOT_USER}:${BUILDROOT_USER} docker/init /init

USER ${BUILDROOT_USER}
ENV HOME /home/${BUILDROOT_USER}
WORKDIR /home/${BUILDROOT_USER}/${BUILDROOT_DIR}

ENTRYPOINT ["/init"]
CMD ["/bin/bash"]

