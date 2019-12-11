FROM centos:7
MAINTAINER Adam Duskett <aduskett@gmail.com>

# Install dependencies
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y \
 flex \
 bison \
 bash \
 wget \
 curl \
 which \
 bzip2 \
 sudo \
 python36 \
 python36-setuptools \
 python36-pip \
 deltarpm \
 git \
 cmake \
 make \
 gcc \
 gcc-c++ \
 unzip \
 file \
 bc \
 patch \
 perl-Data-Dumper \
 perl-ExtUtils-MakeMaker \
 perl-Thread-Queue \
 ncurses-devel \
 glibc.i686 \
 zlib.i686 \
 svn \
 mc

RUN useradd -ms /bin/bash br-user
RUN usermod -aG wheel br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc

USER br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
