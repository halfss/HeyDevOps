#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: hello_servers.py
# Date: Thu 28 Mar 2013 04:24:35 PM CST
# Author: Dong Guo

# Execute: fab -f hello_servers.py set_hosts mytask
from fabric.api import env, run

def set_hosts():
    env.hosts = [
                'dong.guo@localhost:22', 
                'rainbow@heylinux.com:6060'
                ]

def mytask():
    run("/sbin/ifconfig eth0")
