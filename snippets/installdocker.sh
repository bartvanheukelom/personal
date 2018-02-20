#!/bin/bash
# Steps to install Docker CE on Ubuntu
# Source:
#     https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1
set -e

# install dependencies
apt update
apt install apt-transport-https ca-certificates curl software-properties-common

# add repo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
	"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	$(lsb_release -cs) \
	stable"
	
# install Docker
apt update
apt install docker-ce

# install Docker Compose
compver=1.19.0
echo "Press Enter to install Docker Compose $compver @ /usr/local/bin/docker-compose or Ctrl-C to not install"
read
curl -L https://github.com/docker/compose/releases/download/$compver/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

