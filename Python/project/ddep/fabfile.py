#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: fabfile.py
# Date: Thu 28 Mar 2013 10:21:18 PM CST
# Author: Dong Guo

from service import *

def parse_opts():
    """Help message (-h, --help) for fabfile.py."""

    # Import the libraries
    import textwrap
    import argparse

    # The user-defined description
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
        '''
        example:
          ddep -g webserver -H symbio1,symbio2 -r demo_upload
        '''
        ))
    
    # The arguments
    parser.add_argument('-g', metavar='group', type=str,
            help='Deploy to all hosts in the colo-environment group.')
    parser.add_argument('-H', metavar='hosts', type=str,
            help='Verify hosts in specified colo-environment.')
    parser.add_argument('-r', metavar='task', type=str, 
            help='Execute deployment, by default, only print debug output of action to be taken.')

    args = parser.parse_args()
    print args
    
    # Return the values of arguments
    return {'group':args.g, 'host':args.H}

def main():
    opts = parse_opts()

if __name__=='__main__':
    main()
