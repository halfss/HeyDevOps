#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: inventory_execute.py
# Date: Mon 25 Mar 2013 11:37:06 PM CST
# Author: Dong Guo

import MySQLdb

# Create the connection
db = MySQLdb.connect(host='192.168.92.128', db='inventory', user='inventory', 
        passwd='inventory', charset='utf8')
cursor = db.cursor()

# Select
cursor.execute("""SELECT hostname FROM hosts;""")
for row in cursor.fetchall():
    for value in row:
        print value

# Insert
sql = """INSERT IGNORE INTO hosts(hostname,public_dns,colo,environment,`group`,private_ip,public_ip,alias) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"""
param = [
        ("ip-10-197-51-58.us-west-1.compute.internal","ec2-184-169-210-122.us-west-1.compute.amazonaws.com",
            "sc2","dev","webserver","10.197.51.58","184.169.210.122","symbio1"),
        ("ip-10-197-51-26.us-west-1.compute.internal","ec2-54-241-41-87.us-west-1.compute.amazonaws.com",
            "cn1","prod","adserver","10.197.51.26","54.241.41.87","symbio2"),
        ("ip-10-196-13-42.us-west-1.compute.internal","ec2-184-169-192-187.us-west-1.compute.amazonaws.com",
            "va1","qa","apiserver","10.196.13.42","184.169.192.187","symbio3"),
        ("ip-10-197-55-99.us-west-1.compute.internal","ec2-54-241-203-243.us-west-1.compute.amazonaws.com",
            "cn1","prod","apiserver","10.197.55.99","54.241.203.243","symbio4"),
        ("centos","heylinux.com",
            "cn1","dev","blogsite","none","204.74.215.57","myblog")
        ]
execute = cursor.executemany(sql,param)

# Update
sql = """UPDATE hosts SET `group`=%s WHERE hostname=%s;"""
param = ("adserver","ip-10-197-55-99.us-west-1.compute.internal")
execute = cursor.execute(sql,param)

# Delete
sql = """DELETE FROM hosts WHERE hostname=%s"""
param = ("centos")
execute = cursor.execute(sql,param)

# Commit the changes
db.commit()

# Close the cursor
cursor.close()

# Close the connection
db.close()

