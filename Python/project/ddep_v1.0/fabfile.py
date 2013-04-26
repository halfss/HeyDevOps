#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: fabfile.py
# Date: Thu 28 Mar 2013 10:21:18 PM CST
# Author: Dong Guo

import sys
import os

from utils.torndb import Connection
from service.config import dbconf, userconf

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
    task = kwargs['task']

    useropts = userconf()

    if not kwargs.has_key("number"):
        cmd_string = 'fab -u {0} -i {1} -f service/{2}.py -H {3} {4}'.format(useropts["user"],
                useropts["keyfile"],project,host,task)
        print 'Executing \"{0}\"'.format(cmd_string)
        return os.system(cmd_string)
    else:
        number = kwargs["number"]
        cmd_string = 'fab -u {0} -i {1} -f service/{2}.py -H {3} -P -z {4} {5}'.format(useropts["user"],
                useropts["keyfile"],project,host,number,task)
        print 'Executing \"{0}\"'.format(cmd_string)
        return os.system(cmd_string)

def run_task_from_db(opts):
    dbopts = dbconf()
    db = Connection(dbopts["host"], dbopts["database"], dbopts["user"], dbopts["password"])
    sql = """SELECT * FROM hosts WHERE `group` like '{0}'""".format('%%' + opts["group"] + '%%')
    result = []
    for item in db.query(sql):
        result.append(item.public_ip)
    host = ','.join(result)
    if not host:
        print "No host(s) found in group \"{0}\"".format(opts["group"])
        return
    if not opts["number"]:
        return fab_cmd(project=opts["project"],host=host,task=opts["task"])
    return fab_cmd(project=opts["project"],host=host,number=opts["number"],task=opts["task"])

def run_task_from_value(opts):
    if not opts["host"]:
        print "A group or host(s) is required."
        return
    if not opts["number"]:
        return fab_cmd(project=opts["project"],host=opts["host"],task=opts["task"])
    return fab_cmd(project=opts["project"],host=opts["host"],number=opts["number"],task=opts["task"])

def run_task(opts):
    if not opts["group"]:
        return run_task_from_value(opts)
    return run_task_from_db(opts)

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
