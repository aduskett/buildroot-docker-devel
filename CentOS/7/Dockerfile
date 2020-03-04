FROM centos:7
MAINTAINER Adam Duskett <aduskett@gmail.com>

# Install dependencies
RUN yum update -y
RUN yum install -y epel-release
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
  sudo \
  svn \
  tar \
  unzip \
  wget \
  which \
  xz

# 32bit binaries
RUN set -e; \
 yum install -y \
 glibc-devel.i686 \
 libgcc.i686 \
 libstdc++devel.i686 \
 ncurses-devel.i686 \
 zlib.i686 \
 glibc.i686

RUN set -e; \
  yum install -y python-pip; \
  pip install -U pip --prefix=/usr; \
  pip install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2;

# Install GCC8 in case there is a need for gcc > 4.8
RUN set -e; \
 yum install -y \
 centos-release-scl \
 devtoolset-8-gcc-c++ \
 devtoolset-8-libstdc++-devel;

RUN set -e; \
  yum install -y python3-pip; \
  pip3 install -U pip --prefix=/usr; \
  pip3 install \
  nose2==0.9.2 \
  pexpect==4.8.0 \
  spdx_lookup==0.3.2;

RUN set -e; \
  useradd -ms /bin/bash br-user; \
  echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc;

RUN set -e; \
  chown -R br-user:br-user /home/br-user; \
  echo "alias ls='ls --color=auto'" >> /root/.bashrc; \
  echo "PS1='\u@\H [\w]$ '" >> /root/.bashrc

COPY brmake /usr/bin

USER br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
