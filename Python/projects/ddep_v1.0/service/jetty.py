#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: jetty.py
# Date: Sat 30 Mar 2013 07:32:14 PM CST
# Author: Dong Guo

from fabric.api import sudo
from fabric.colors import green

def start():
    print(green("Start Jetty"))
    sudo('/etc/init.d/jetty start')

def stop():
    print(green("Stop Jetty"))
    sudo('/etc/init.d/jetty stop')

def restart():
    print(green("Restart Jetty"))
    sudo('/etc/init.d/jetty restart')

def status():
    print(green("Check Jetty"))
    sudo('/etc/init.d/jetty check')
