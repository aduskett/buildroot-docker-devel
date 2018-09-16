FROM centos:6
MAINTAINER Adam Duskett <aduskett@gmail.com>

# Install dependencies
RUN yum update -y
RUN yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN yum install -y \
    flex bison bash yum wget curl which bzip2 sudo deltarpm git \
    cmake make gcc gcc-c++ unzip file bc patch perl-Data-Dumper perl-ExtUtils-MakeMake \
    python-pip ncurses-devel

RUN pip install argparse 

RUN useradd buildroot
RUN usermod -aG wheel buildroot

# Install Buildroot.
RUN git clone git://git.buildroot.net/buildroot /home/buildroot/buildroot
RUN echo "alias ls='ls --color=auto'" >> /home/buildroot/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/buildroot/.bashrc
RUN chown -R buildroot:buildroot /home/buildroot

CMD ["/bin/sh"]
