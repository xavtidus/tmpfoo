#!/bin/bash

cd /home/ubuntu
touch starting.setup.done

sudo apt update -y && sudo apt upgrade -y
touch update.setup.done

sudo apt install python3-pip -y
touch pypip3.setup.done

sudo apt install git -y
touch git.setup.done

sudo apt install awscli -y
touch awscli.setup.done

git clone https://github.com/xavtidus/tmpfoo.git
touch gitclone.setup.done

cd tmpfoo
touch cd.setup.done

pip3 install -r requirements.txt 
touch requirements.pip.setup.done

pip3 install opencv-contrib-python
touch opencv.pip.setup.done

pip3 install awscli --upgrade
touch awscliupdate.pip.setup.done

sudo apt-get install libopencv-* -y
touch startcv.pip.setup.done
