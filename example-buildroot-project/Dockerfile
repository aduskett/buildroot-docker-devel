FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=UTC

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
  python3-aiohttp \
  python3-cvelib \
  python3-ijson \
  python3-nose2 \
  python3-pexpect \
  python3-requests \
  rsync \
  subversion \
  sudo \
  tar \
  unzip \
  wget \
  zip \
  gcc-multilib \
  g++-multilib \
  libc6-i386;

RUN set -e; \
  pip3 install --force --break-system-packages \
  spdx_lookup==0.3.3;

# Set these arguments in the docker-compose.yml file and the docker/env file
# if you wish to change the default values.
# Default values:
# BUILDROOT_USER: br-user
# BUILDROOT_DIR: buildroot
# BUILDROOT_VERSION: If set to git, clone from the repo
# The buildroot source code is extracted to /home/${BUILDROOT_USER}/{BUILDROOT_DIR}
ARG BUILDROOT_USER
ARG BUILDROOT_DIR
ARG BUILDROOT_VERSION=2023.02.2
ARG BUILDROOT_BRANCH=master
ARG UID=1000
ARG GID=1000

# Add the ${BUILDROOT_USER} user, as buildroot should never be built as root.
RUN /bin/bash; \
  set -e; \
  usermod -u 9955 ubuntu; \
  groupmod -g 9955 ubuntu; \
  groupadd -r -g ${GID} ${BUILDROOT_USER}; \
  useradd -ms /bin/bash -u ${UID} -g ${GID} ${BUILDROOT_USER}; \
  echo "alias ls='ls --color=auto'" >> /home/${BUILDROOT_USER}/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/${BUILDROOT_USER}/.bashrc; \
  chown -R ${BUILDROOT_USER}:${BUILDROOT_USER} /home/${BUILDROOT_USER}; \
  if [ $BUILDROOT_VERSION = "git" ]; then \
    echo "Cloning Buildroot on branch ${BUILDROOT_BRANCH}"; \
    git clone git://git.buildroot.net/buildroot /home/${BUILDROOT_USER}/buildroot -b ${BUILDROOT_BRANCH}; \
  else \
    wget https://buildroot.org/downloads/buildroot-${BUILDROOT_VERSION}.tar.xz -O /home/${BUILDROOT_USER}/buildroot.tar.xz; \
    mkdir -p /home/${BUILDROOT_USER}/${BUILDROOT_DIR}; \
    tar -Jxf /home/${BUILDROOT_USER}/buildroot.tar.xz --strip-components=1 -C /home/${BUILDROOT_USER}/${BUILDROOT_DIR}; \
    rm -rf /home/${BUILDROOT_USER}/buildroot.tar.xz; \
  fi; \
  chown -R ${BUILDROOT_USER}:${BUILDROOT_USER} /home/${BUILDROOT_USER}/${BUILDROOT_DIR};

# Copy brmake to /usr/bin for non-verbose builds.
WORKDIR /home/${BUILDROOT_USER}/${BUILDROOT_DIR}
RUN set -e; \
  cp utils/brmake /usr/bin/brmake; \
  chmod +x /usr/bin/brmake;

# Perform the following:
# - Pre-emtpively create the ccache diretory for permission purposes.
# - Link each external_tree to the base buildroot directory.
ARG EXTERNAL_TREES
RUN set -e; \
  mkdir -p /home/${BUILDROOT_USER}/ccache; \
  chown -R ${BUILDROOT_USER}:${BUILDROOT_USER} /home/${BUILDROOT_USER}/ccache; \
  mkdir -p /tmp/patches; \
  for tree in ${EXTERNAL_TREES}; do \
    ln -sf /mnt/${tree} ${tree}; \
  done;

# Ensure that any patches held in ${external_trees}/patches/buildroot are applied.
# This ensures that relevant upstream patches cherry-picked from
# https://patchwork.ozlabs.org/project/buildroot/list/ are applied during the
# docker build process.
ARG BUILDROOT_PATCH_DIR
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

