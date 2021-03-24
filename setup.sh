#!/bin/bash

cd ~/

sudo apt update -y && sudo apt upgrade -y

sudo apt install python3-pip -y

sudo apt install git -y

sudo apt  install awscli -y

git clone https://github.com/xavtidus/tmpfoo.git

cd tmpfoo

pip3 install -r requirements.txt 

pip3 install opencv-contrib-python
