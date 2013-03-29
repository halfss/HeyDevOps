#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: demo.py
# Date: Fri 29 Mar 2013 04:51:25 AM CST
# Author: Dong Guo

# Usage: fab -f demo.py -H dong.guo@localhost:22 demo_upload
from fabric.api import *
from fabric.colors import green
from conf import global_settings

settings = global_settings

def demo_upload():
    print(green("Transfer the file demo_upload.txt"))
    with lcd (settings.PROJECT_HOME):
        put('data/demo/demo_upload.txt','/tmp/') 

def main():
    execute(demo_upload)

if __name__=='__main__':
    main()
