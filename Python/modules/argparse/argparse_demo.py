#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: argparse_demo.py
# Date: Thu 28 Mar 2013 11:34:37 PM CST
# Author: Dong Guo

import textwrap
import argparse

def parse_opts():
    """Help messages (-h, --help) for fabfile.py."""
    
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
    return {'group':args.g, 'host':args.H, 'project':args.r, 'task':args.t, 'number':args

def main():
    opts = parse_opts()

if __name__=='__main__':
    main()
