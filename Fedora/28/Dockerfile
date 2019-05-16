FROM fedora:28
MAINTAINER Adam Duskett <aduskett@gmail.com>

LABEL maintainer="Adam Duskett <aduskett@gmail.com>" \
description="Container with everything needed to run Buildroot"

# Install dependencies
RUN dnf update -y
RUN dnf install -y \
 flex \
 bison \
 wget \
 which \
 bzip2 \
 sudo \
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
 cpio \
 python \
 rsync \
 svn

RUN useradd -ms /bin/bash br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc
RUN chown -R br-user:br-user /home/br-user

USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]

