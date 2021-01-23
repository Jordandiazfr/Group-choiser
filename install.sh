#!/usr/bin/env bash 
echo Installing GroupChoiser
cd groupchoisersetup
python setup.py install
pip install .
groupchoiser
read -p "Press enter to exit"
