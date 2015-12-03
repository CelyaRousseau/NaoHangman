#!/bin/sh
cd /tmp/

wget https://pypi.python.org/packages/source/s/setuptools/setuptools-18.7.1.tar.gz -O setuptools.tar.gz
wget https://pypi.python.org/packages/source/U/Unidecode/Unidecode-0.04.18.tar.gz -O unidecode.tar.gz

tar -xzf setuptools.tar.gz -C /tmp/
tar -xzf unidecode.tar.gz -C /tmp/

cd setuptools-18.7.1/
sudo python2 setup.py install
cd Unidecode-0.04.18/
sudo python2 setup.py install
