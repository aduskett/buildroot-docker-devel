FROM centos:7
MAINTAINER Bilge <bilge@scriptfusion.com>

WORKDIR /root

# Install dependencies.
RUN yum update && yum install -y "Development Tools"
RUN yum install -y flex bison bash

# Install Buildroot.
RUN wget -nv https://buildroot.org/downloads/buildroot-2018.08.tar.bz2 &&\
    tar xf buildroot-*.tar* &&\
    rm buildroot-*.tar* &&\
    ln -s buildroot-* buildroot


# Install BusyBox.
RUN wget -nv https://busybox.net/downloads/busybox-1.26.2.tar.bz2 &&\
    tar xf *.tar* &&\
    rm *.tar* &&\
    ln -s busybox-* busybox &&\
    ln -s ~/busybox/.config /etc/busybox.conf

RUN echo "alias ll='ls --color=auto'" >> .bashrc
