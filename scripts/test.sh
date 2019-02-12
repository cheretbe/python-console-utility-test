#!/bin/bash

mkdir -p ~/temp
pushd ~/temp
git clone https://github.com/cheretbe/multi-ip-ddclient.git
pushd multi-ip-ddclient
popd
popd
which pip3
make init-dev