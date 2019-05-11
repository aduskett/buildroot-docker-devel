FROM centos:6
MAINTAINER Adam Duskett <aduskett@gmail.com>

# Install dependencies
RUN yum update -y
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN yum install -y centos-release-scl
RUN yum install -y \
 flex \
 bison \
 bash \
 yum \
 wget \
 curl \
 which \
 bzip2 \
 sudo \
 deltarpm \
 git \
 cmake \
 make \
 gcc \
 gcc-c++ \
 unzip \
 file \
 bc \
 xz \
 patch \
 perl-Data-Dumper \
 perl-ExtUtils-MakeMaker \
 perl-Thread-Queue \
 ncurses-devel \
 nano \
 rh-python36-python-pip \
 python27

RUN wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-el6/epel-6-x86_64/glibc-2.17-55.fc20/glibc-2.17-55.el6.x86_64.rpm
RUN wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-el6/epel-6-x86_64/glibc-2.17-55.fc20/glibc-common-2.17-55.el6.x86_64.rpm
RUN wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-el6/epel-6-x86_64/glibc-2.17-55.fc20/glibc-devel-2.17-55.el6.x86_64.rpm
RUN wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-el6/epel-6-x86_64/glibc-2.17-55.fc20/glibc-headers-2.17-55.el6.x86_64.rpm

RUN sudo rpm -Uvh glibc-2.17-55.el6.x86_64.rpm \
 glibc-common-2.17-55.el6.x86_64.rpm \
 glibc-devel-2.17-55.el6.x86_64.rpm \
 glibc-headers-2.17-55.el6.x86_64.rpm

RUN sudo rm *.rpm

RUN useradd -ms /bin/bash br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc

RUN yum install -y python-pip
RUN pip install argparse

RUN echo "source /opt/rh/rh-python36/enable" >> /home/br-user/.bashrc
RUN echo "source /opt/rh/python27/enable" >> /home/br-user/.bashrc
RUN echo "source /opt/rh/rh-python36/enable" >> /root/.bashrc
RUN echo "source /opt/rh/python27/enable" >> /root/.bashrc

RUN chown -R br-user:br-user /home/br-user
RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /root/.bashrc

USER br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
