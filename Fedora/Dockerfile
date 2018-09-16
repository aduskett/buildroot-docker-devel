FROM fedora:28
MAINTAINER Adam Duskett <aduskett@gmail.com>

# Install dependencies
RUN dnf update -y
RUN dnf install -y \
    flex bison bash dnf wget curl which bzip2 sudo git \
    cmake make gcc gcc-c++ unzip file bc patch \
    perl-Data-Dumper perl-ExtUtils-MakeMaker perl-Thread-Queue \
    ncurses-devel

RUN useradd buildroot
RUN usermod -aG wheel buildroot

# Install Buildroot.
 RUN wget -nv https://buildroot.org/downloads/buildroot-2018.08.tar.bz2 &&\
    tar xf buildroot-*.tar* &&\
    rm buildroot-*.tar* &&\
    mv buildroot-* /home/buildroot/buildroot

RUN echo "alias ls='ls --color=auto'" >> /home/buildroot/.bashrc
RUN chown -R buildroot:buildroot /home/buildroot

CMD ["/bin/sh"]

