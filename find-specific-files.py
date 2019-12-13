#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   find-specific-files.py
# Purpose:     get files with specific filters under specific directory   
#
# Author:      Ke Wang
#
# Created:     2019-10-14
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os 
import fnmatch

def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

def find_specific_files(root, patterns=['*'],exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)
    for d in exclude_dirs:
        if d in dirnames:
            dirnames.remove(d)

def main():
    # Get all files under current directory
    for item in find_specific_files("."):
        print(item)
    # Get all python files under current directory
    patterns = ['*.py']
    for item in find_specific_files(".", patterns):
        print(item)
    # Get all log files under current directory excluding anaconda
    patterns = ['*.log']
    exclude_dirs = ['anaconda']
    for item in find_specific_files("/var/log", patterns):
        print(item)

    # Get top 10 maximum size files
    files = {name: os.path.getsize(name) for name in
             find_specific_files('/var/log')} 
    result = sorted(files.items(),key=lambda d:d[1], reverse=True)[:10]
    for i,t in enumerate(result,1): 
        print(i, t[0],t[1])

if __name__ == '__main__':
    main()
