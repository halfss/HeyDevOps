#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: hello_fabric.py
# Date: Thu 28 Mar 2013 04:06:13 PM CST
# Author: Dong Guo

# Usage: fab -f hello_fabric.py hello:name=Fabric
def hello(name="world"):
    print("Hello %s!" % name)
