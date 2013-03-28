#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: inventory_execute.py
# Date: Thu 28 Mar 2013 02:56:06 PM CST
# Author: Dong Guo

import MySQLdb

class Inventory(object):
    """
    # Select
    db.select("SELECT hostname FROM hosts;")

    # Insert, Update, Delete
    sql = 'INSERT IGNORE INTO hosts(hostname,public_dns,colo,environment,`group`,private_ip,public_ip,alias) 
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'
    param = [
            ("ip-10-197-51-58.us-west-1.compute.internal",
             "ec2-184-169-210-122.us-west-1.compute.amazonaws.com",
             "sc2","dev","webserver","10.197.51.58","184.169.210.122","symbio1"),
            ("ip-10-197-51-26.us-west-1.compute.internal",
             "ec2-54-241-41-87.us-west-1.compute.amazonaws.com",
             "cn1","prod","adserver","10.197.51.26","54.241.41.87","symbio2"),
            ]
    db.execute(sql,param)
    """

    HOST = '192.168.92.128'
    DB = 'inventory'
    USER = 'inventory'
    PWD = 'inventory'
    CHARSET = 'utf8'

    def __init__(self):
        self._conn = None
        if not self._create_connect():
            print 'Failed to connect.'

    def __del__(self):
        if not self._conn:
            self._conn.close()

    # Create the connection
    def _create_connect(self):
        try:
            self._conn = MySQLdb.connect(
                            host = self.HOST,
                            db = self.DB, 
                            user = self.USER, 
                            passwd = self.PWD,
                            charset = self.CHARSET)
        except MySQLdb.Error, e:
            print '{0}'.format(e)
            return False
        else:
            return True

    def _commit(self):
        self._conn.commit()

    # Select
    def select(self, sql):
        try:
            cursor = self._conn.cursor()
            cursor.execute(sql)
            self._commit()
            for row in cursor.fetchall():
                for value in row:
                    print value
        except MySQLdb.Error, e:
            print '{0}'.format(e)
            return False
        else:
            return True
                
    # Execute - Insert,Update,Delete
    def execute(self, sql, param):
        try:
            cursor = self._conn.cursor()
            execute = cursor.executemany(sql,param)
            self._commit()
        except MySQLdb.Error, e:
            print '{0}'.format(e)
            return False
        else:
            return True
