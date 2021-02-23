#!/bin/sh

sed -i s/disnocen/$USER/ freefolio.py
mkdir -p $HOME/bin && cp freefolio.py $HOME/bin
echo "freefolio.py copied in $HOME/bin. Be sure that $HOME/bin is in your PATH"  
echo "Installing pycoingecko"  
which pip3 && pip3 install pycoingecko || echo "install python3-pip before going on"  
mkdir $HOME/.config/freefolio && cp config.example $HOME/.config/freefolio/config
echo "you should modify the config file in $HOME/.config/freefolio/config"  
