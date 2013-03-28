#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: server_config.py
# Date: Thu 28 Mar 2013 03:19:18 PM CST
# Author: Dong Guo

import ConfigParser

config = ConfigParser.ConfigParser()

# Read server.ini
config.read("server.ini")

# Return all section
sections = config.sections()
print "Sections:", sections

options = config.options("author")
print "Options:", options

keyvalues = config.items("author")
print "Author:", keyvalues

# Read by type
string_value = config.get("author", "name")
int_value = config.getint("author", "id")

print "Value for author's name:", string_value
print "Value for author's id:", int_value

# Write config
# Update value
config.set("author", "id", "009")
# Set a new value
config.set("author", "title", "system administrator")
# Create a new section
config.add_section("role")
config.set("role", "webserver", "symbio1")
# Write back to configure file
config.write(open("server.ini", "wb"))
