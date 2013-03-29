#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: config.py
# Date: Fri 29 Mar 2013 07:26:50 AM CST
# Author: Dong Guo

import os
import ConfigParser
from conf import global_settings

config = ConfigParser.ConfigParser()

settings = global_settings

def dbconf(key):
    try:
        file = os.path.join(settings.CONFIG_HOME, 'db.ini')
        config.read(file)
        value = config.get("default", key)
    except ConfigParser.Error, e:
        print '{0}'.format(e)
        return False
    else:
        return value
