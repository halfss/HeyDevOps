#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: host_type.py
# Date: Thu 28 Mar 2013 04:06:43 PM CST
# Author: Dong Guo

# Execute: fab -f host_type.py -H dong.guo@localhost:22 host_type
from fabric.api import run

def host_type():
    run('uname -s')
