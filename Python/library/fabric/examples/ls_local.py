#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: ls_local.py
# Date: Thu 28 Mar 2013 04:12:04 PM CST
# Author: Dong Guo

# Usage: fab -f ls_local.py lslocal
from fabric.api import local

def lslocal():
    local('ls -l')
