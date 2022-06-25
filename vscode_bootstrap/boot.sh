#!/bin/bash

# this will bootstrap a debian based docker container
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

# this is a crude check to see if the pyenv already exists.
# if does (2nd run) it will skip this putting it in the .bashrc
FILE1=/home/vscode/.pyenv/libexec/pyenv
if [ ! -f $FILE1 ]
then
	cat pyenvbash >> ~/.bashrc
fi

FILE2=/home/vscode/.pyenv/versions/3.11.0b3/bin/python3
if [ ! -f $FILE2 ]
then
	curl -Lq https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
	source ~/.bashrc

	# install beta version of python3.11 for speed
	pyenv install 3.11.0b3

	# create a good symlink
	sudo ln -s /home/vscode/.pyenv/versions/3.11.0b3/bin/python3 /usr/local/bin/python3.11
else
	echo "skipping install of python3.11.  Found a binary..."
fi

echo "dockervscode_bootstrap.sh completed."
