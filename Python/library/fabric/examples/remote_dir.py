#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: remote_dir.py
# Date: Thu 28 Mar 2013 04:16:25 PM CST
# Author: Dong Guo

# Execute: fab -f remote_dir.py -H dong.guo@localhost:22 filepath
from fabric.api import cd, run

def filepath():
    remote_dir = '/home/dong.guo'
    with cd(remote_dir):
        run("ls -l")
