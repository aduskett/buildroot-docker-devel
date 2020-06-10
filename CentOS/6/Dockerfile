FROM centos:6
MAINTAINER Adam Duskett <aduskett@gmail.com>

# Install dependencies
RUN yum update -y
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN yum install -y \
  bash \
  bc \
  bison \
  bzip2 \
  cmake \
  cpio \
  curl \
  dialog \
  deltarpm \
  expect \
  file \
  flex \
  gcc \
  gcc-c++ \
  git \
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
  wget \
  which \
  xz

# 32bit gcc >= 4.9 support
COPY copr-gcc8.repo /etc/yum.repos.d/
RUN set -e; \
  yum install -y \
  glibc-devel.i686 \
  devtoolset-8-gcc-c++ \
  devtoolset-8-libstdc++-devel.i686

RUN set -e; \
  yum install -y centos-release-scl; \
  yum install -y \
  python27 \
  rh-python36-python-pip;

RUN set -e; \
  PATH=/opt/rh/python27/root/usr/bin${PATH:+:${PATH}} \
  LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} \
  PKG_CONFIG_PATH=/opt/rh/python27/root/usr/lib64/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}} \
  /opt/rh/python27/root/usr/bin/pip2 install -U pip;

RUN set -e; \
  PATH=/opt/rh/python27/root/usr/bin${PATH:+:${PATH}} \
  LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} \
  PKG_CONFIG_PATH=/opt/rh/python27/root/usr/lib64/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}} \
  /opt/rh/python27/root/usr/bin/pip2 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2;

RUN set -e; \
  PATH=/opt/rh/rh-python36/root/usr/bin${PATH:+:${PATH}} \
  LD_LIBRARY_PATH=/opt/rh/rh-python36/root/usr/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} \
  PKG_CONFIG_PATH=/opt/rh/rh-python36/root/usr/lib64/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}} \
  /opt/rh/rh-python36/root/usr/bin/pip3 install -U pip;

RUN set -e; \
  PATH=/opt/rh/rh-python36/root/usr/bin${PATH:+:${PATH}} \
  LD_LIBRARY_PATH=/opt/rh/rh-python36/root/usr/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} \
  PKG_CONFIG_PATH=/opt/rh/rh-python36/root/usr/lib64/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}} \
  /opt/rh/rh-python36/root/usr/bin/pip3 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2;

RUN set -e; \
  useradd -ms /bin/bash br-user; \
  echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc; \
  echo "source /opt/rh/python27/enable" >> /home/br-user/.bashrc; \
  echo "source /opt/rh/python27/enable" >> /root/.bashrc; \
  echo "source /opt/rh/rh-python36/enable" >> /home/br-user/.bashrc; \
  echo "source /opt/rh/rh-python36/enable" >> /root/.bashrc; \
  echo "source /opt/rh/devtoolset-8/enable" >> /home/br-user/.bashrc; \
  echo "source /opt/rh/devtoolset-8/enable" >> /root/.bashrc;

RUN set -e; \
  chown -R br-user:br-user /home/br-user; \
  echo "alias ls='ls --color=auto'" >> /root/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /root/.bashrc

COPY brmake /usr/bin

USER br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
