#!/bin/bash

sudo apt-get -y update
sudo apt-get -y install build-essential libapt-pkg-dev libffi-dev libssl-dev python-dev 
wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
sudo python /tmp/get-pip.py
rm -v /tmp/get-pip.py
sudo pip install virtualenv
virtualenv $HOME/ 
wget http://archive.ubuntu.com/ubuntu/pool/main/p/python-apt/python-apt_1.1.0~beta1build1.tar.xz -O /tmp/papt.txz
cd /tmp; tar xf /tmp/papt.txz
$HOME/bin/pip install sphinx 
$HOME/bin/pip install http://archive.ubuntu.com/ubuntu/pool/universe/p/python-distutils-extra/python-distutils-extra_2.39.orig.tar.gz 
$HOME/bin/pip install /tmp/python-apt-1.1.0~beta1
$HOME/bin/pip install ansible 
