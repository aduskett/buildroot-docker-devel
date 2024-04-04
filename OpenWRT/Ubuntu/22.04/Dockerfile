FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=US/Pacific

RUN set -e; \
  apt-get update; \
  apt-get install -y apt-utils; \
  apt-get upgrade -y; \
  apt-get install -y locales;

RUN set -e; \
  rm -rf /var/lib/apt/lists/*; \
  localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

# Setup tzdata first as to avoid a dialog requesting tzdata setup.
RUN set -e; \
  apt-get update; \
  apt-get install -y tzdata; \
  ln -snf /usr/share/zoneinfo/$TZ /etc/localtime; \
  echo $TZ > /etc/timezone;

# Install dependencies
RUN set -e; \
  apt-get update; \
  apt-get upgrade -y; \
  apt-get install -y \
    bison \
    build-essential \
    ccache \
    clang \
    file \
    flex \
    g++ \
    gawk \
    gcc-multilib \
    gettext \
    git \
    g++-multilib \
    libncurses-dev \
    libssl-dev \
    llvm \
    nano \
    python3-cryptography \
    python3-distutils \
    python3-jsonschema \
    python3-pip \
    python3-pyelftools \
    python3-yaml \
    rsync \
    swig \
    unzip \
    wget \
    zlib1g-dev;

RUN set -e; \
  pip3 install -U pip; \
  pip3 install pylibfdt;

RUN useradd -ms /bin/bash wrt-user
RUN echo "alias ls='ls --color=auto'" >> /home/wrt-user/.bashrc
RUN echo "PS1='\u@\H [\w]$ '" >> /home/wrt-user/.bashrc
COPY quiltrc /home/wrt-user/.quiltrc
RUN chown -R wrt-user:wrt-user /home/wrt-user

RUN set -e; \
  mkdir -p /home/ccache; \
  chown -R wrt-user:wrt-user /home/ccache;

USER wrt-user
WORKDIR /home/wrt-user
ENV HOME /home/wrt-user

CMD ["/bin/bash"]
