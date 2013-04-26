#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: fabfile.py
# Date: Thu 28 Mar 2013 10:21:18 PM CST
# Author: Dong Guo

import sys
import os

from utils.torndb import Connection
from service.config import dbconf

def parse_opts():
    """Help messages (-h, --help) for fabfile.py."""
    
    # import the libraries
    import textwrap
    import argparse

    # the user-defined description
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
        '''
        example:
          ddep -H symbio1,symbio2,symbio3 -r demo -t upload
          ddep -g webserver -r demo -t upload
          ddep -g webserver -r demo -t upload -f 2
        '''
        ))
    
    exclusion = parser.add_mutually_exclusive_group()

    # the arguments
    exclusion.add_argument('-g', metavar='group', type=str,
            help='Deploy to all hosts in the group.')
    exclusion.add_argument('-H', metavar='hosts', type=str,
            help='Deploy to the hosts.')
    parser.add_argument('-r', metavar='project', type=str, required=True,
            help='Execute the project.')
    parser.add_argument('-t', metavar='task', type=str, required=True,
            help='The task name of the project.')
    parser.add_argument('-f', metavar='number', type=int, 
            help='The number of concurrent processes to use in parallel mode.')

    args = parser.parse_args()
    
    # return the values of arguments
    return {'group':args.g, 'host':args.H, 'project':args.r, 'task':args.t, 'number':args.f}

def fab_cmd(**kwargs):
    project = kwargs['project']
    host = kwargs['host']
    number = kwargs['number']
    task = kwargs['task']

    if not number:
        cmd_string = ("fab -f service/%s.py -H %s %s" % (project,host,task))
        print("Executing \"%s\"" % cmd_string)
        os.system(cmd_string)
    else:
        cmd_string = ("fab -f service/%s.py -H %s -P -z %s %s" % (project,host,number,task))
        print("Executing \"%s\"" % cmd_string)
        os.system(cmd_string)

def run_task(opts):
    project = opts["project"]
    task = opts["task"]

    group = opts["group"]
    if not group:
        host = opts["host"]
        if not host:
            print "A group or host(s) is required."
            return None
        else:
            number = opts["number"]
            if not number:
                fab_cmd(project=project,host=host,task=task)
            else:
                fab_cmd(project=project,host=host,number=number,task=task)
    else:
        dbopts = dbconf()
        host = dbopts["host"]
        database = dbopts["database"]
        user = dbopts["user"]
        password = dbopts["password"]
        db = Connection(host,database,user,password)
        sql = ("""SELECT * FROM hosts WHERE `group` like '%s'""" % ('%%' + group + '%%'))
        str = []
        for item in db.query(sql):
            str.append(item.public_ip)
        host = ','.join(str)
        if not host:
            print ("No host(s) found in group \"%s\"" % group)
            return None
        number = opts["number"]
        if not number:
            fab_cmd(project=project,host=host,task=task)
        else:
            fab_cmd(project=project,host=host,number=number,task=task)

def main():
    # check if user executes the script without any arguments
    argv_len = len(sys.argv)
    if argv_len < 2:
        os.system("./ddep -h")
        return None 

    opts = parse_opts()
    run_task(opts)

if __name__=='__main__':
    main()
