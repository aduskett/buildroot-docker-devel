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
 curl \
 deltarpm \
 expect \
 file \
 flex \
 gcc \
 gcc-c++ \
 git \
 glibc.i686 \
 make \
 mc \
 ncurses-devel \
 patch \
 perl-Data-Dumper \
 perl-ExtUtils-MakeMaker \
 perl-Thread-Queue \
 python36 \
 python36-setuptools \
 sudo \
 svn \
 unzip \
 wget \
 which \
 zlib.i686

# Install GCC9 in case there is a need for gcc > 4.8
RUN set -e; \
 yum install -y centos-release-scl; \
 yum install -y devtoolset-9-gcc-c++;

RUN pip3 install -U pip --prefix=/usr

RUN useradd -ms /bin/bash br-user
RUN usermod -aG wheel br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc

COPY brmake /usr/bin

USER br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
