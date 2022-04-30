#!/bin/bash

echo "bootstrap.sh started..."

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
    
apt-get update 
apt-get upgrade -y 
apt-get install -y \
    ca-certificates \
    ssh \
    tmux \
    vim \
    curl \
    htop \
    build-essential \
    python3-venv \
    python3-dev \
    python3-pip \
    git \
    gnupg \
    lsb-release \
    wget \
    libssl-dev

FILE=/etc/apt/sources.list.d/docker.list    

# install docker
if [ ! -f $FILE ]
then
    
    echo "starting to install docker..."
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    sudo usermod -aG docker youtube

    echo "docker install completed."
else
    echo "docker is already installed skipping..."
fi

echo "bootstrap.sh completed."
