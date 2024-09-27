#!/bin/bash

# 下载PyInstaller源码
cd /tmp
curl -LO https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v4.10.tar.gz
tar -xzvf v4.10.tar.gz
cd pyinstaller-4.10/bootloader

# 编译PyInstaller引导程序
python3 ./waf configure
python3 ./waf all
python3 ./waf install
