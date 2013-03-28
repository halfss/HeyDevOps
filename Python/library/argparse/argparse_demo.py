#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: argparse_demo.py
# Date: Thu 28 Mar 2013 11:34:37 PM CST
# Author: Dong Guo

import textwrap
import argparse

def parse_opts():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
        '''
        deployment engine should run as:
        "ddep -c config [-g group] [-H host [host1,host2,host3]] [-r]"
        '''
        ))
    parser.add_argument('-c', metavar='config', type=str, required=True,
            help='Read the configuration from a specific file, by default, it\'s from database.')
    parser.add_argument('-g', metavar='group', type=str,
            help='Deploy to all hosts in the colo-environment group.')
    parser.add_argument('-H', metavar='host [host1,host2,host3...]', type=str,
            help='Verify hosts in specified colo-environment.')
    parser.add_argument('-r', action='store_true', 
            help='Execute deployment, by default, only print debug output of action to be taken.')
    args = parser.parse_args()
    print args
    return {'config':args.c, 'group':args.g, 'host':args.H}

def main():
    opts = parse_opts()

if __name__=='__main__':
    main()
