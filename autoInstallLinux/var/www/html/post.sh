#!/bin/bash

# docker
sudo apt-get update
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
sudo apt-get install -y docker-engine
sudo usermod -aG docker youtube

# golang 
wget --quiet https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.8.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> /home/youtube/.bashrc
echo 'export GOBIN=/root/go/bin' >> /home/youtube/.bashrc
echo 'export GOPATH=/root/go/bin' >> /home/youtube/.bashrc
rm go1.8.linux-amd64.tar.gz
