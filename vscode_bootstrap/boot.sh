#!/bin/bash

# this will bootstrap a debian based docker container
SECONDS=0

clear
echo "dockervscode_bootstrap.sh started..."

# apt-get
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -yq \
    curl \
    wget \
    git \
    python3-pip \
    python3-dev \
    build-essential \
    gcc \
    vim \
    tmux \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
	libreadline-dev \
	libsqlite3-dev \
	llvm \
	libncurses5-dev \
	libncursesw5-dev \
	xz-utils tk-dev \
	libffi-dev \
	liblzma-dev

# this will kinda check if this script already ran
# if you want to run this part remove .pyenv folder
# also remove symlink generated below.
FILE1=/home/vscode/.pyenv/libexec/pyenv
if [ ! -f $FILE1 ]
then
	cat pyenvbash >> ~/.bashrc
	curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
	# source ~/.bashrc

	# install python3.11
	export PYENV_ROOT="$HOME/.pyenv" && \
	export PATH="$PYENV_ROOT/bin:$PATH" && \
	eval "$(pyenv init --path)" && \
	eval "$(pyenv init -)" && \
	pyenv install 3.11.0b3

	sudo ln -s /home/vscode/.pyenv/versions/3.11.0b3/bin/python3 /usr/local/bin/python3.11
else
	echo "skipping installation .pyenv exists.  delete this and the symlink to run again..."
fi
duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo "dockervscode_bootstrap.sh completed."