FROM centos:6
MAINTAINER Adam Duskett <aduskett@gmail.com>

# Install dependencies
RUN yum update -y
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
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
 ncurses-devel

RUN useradd -ms /bin/bash br-user
RUN echo "alias ls='ls --color=auto'" >> /home/br-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/br-user/.bashrc

RUN yum install -y python-pip
RUN pip install argparse

# RUN yum install -y centos-release-scl
# RUN yum install -y python27
# RUN LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64/:$LD_LIBRARY_PATH /opt/rh/python27/root/usr/bin/easy_install-2.7 pip
# RUN ln -s /opt/rh/python27/root/usr/bin/pip2.7 /usr/bin/pip
# RUN LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64/:$LD_LIBRARY_PATH pip install --upgrade pip
# RUN LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64/:$LD_LIBRARY_PATH pip install argparse 
# RUN cat /opt/rh/python27/enable >> /home/br-user/.bashrc
# RUN cat /opt/rh/python27/enable >> /root/.bashrc

RUN chown -R br-user:br-user /home/br-user
RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /root/.bashrc

USER br-user
WORKDIR /home/br-user
ENV HOME /home/br-user
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
