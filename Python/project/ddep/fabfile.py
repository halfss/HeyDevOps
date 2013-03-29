#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: fabfile.py
# Date: Thu 28 Mar 2013 10:21:18 PM CST
# Author: Dong Guo

from fabric.api import env, local
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
          ddep -H symbio1,symbio2,symbio3 -r demo_upload
          ddep -g webserver -r demo_upload
        '''
        ))
    
    exclusion = parser.add_mutually_exclusive_group()

    # the arguments
    exclusion.add_argument('-g', metavar='group', type=str,
            help='Deploy to all hosts in the colo-environment group.')
    exclusion.add_argument('-H', metavar='hosts', type=str,
            help='Verify hosts in specified colo-environment.')
    parser.add_argument('-r', metavar='task', type=str, 
            help='Execute deployment, by default, only print debug output of action to be taken.')

    args = parser.parse_args()
    
    # return the values of arguments
    return {'group':args.g, 'host':args.H, 'task':args.r}

def run_task(opts):
    task = opts["task"]
    print("task is %s" % task)

    if task == None:
        print "no task given"
    else:
        group = opts["group"]
        if group == None:
            print "no group given"
            host = opts["host"]
            if host == None:
                print "no host given"
                return None
            else:
                print("fab -f service/%s.py -H %s %s" % (task,host,task))
                local("fab -f service/%s.py -H %s %s" % (task,host,task))
        else:
            dbopts = dbconf()
            host = dbopts["host"]
            database = dbopts["database"]
            user = dbopts["user"]
            password = dbopts["password"]
            db = Connection(host,database,user,password)
            sql = ('SELECT * FROM hosts WHERE `group`="%s"' % group)
            for item in db.query(sql):
                hosts = item.public_dns
                print("fab -f service/%s.py -H %s %s" % (task,hosts,task))
                local("fab -f service/%s.py -H %s %s" % (task,hosts,task))

def main():
    opts = parse_opts()
    run_task(opts)

if __name__=='__main__':
    main()
