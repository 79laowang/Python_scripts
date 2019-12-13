#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        make_text_file.py
# Purpose:     create a text file and write input to a text file
#
# Author:      Ke Wang
#
# Created:     06/07/2019
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import os
# Replacing module variables with local variables, good performance
ls = os.linesep


def main():
    # get filename
    while True:
        fname = input('Enter filename: ')
        if os.path.exists(fname):
            print("ERROR: '%s' already exists" % fname)
        else:
            break

    # get file content (text) lines
    all = []
    print("\nEnter lines ('.' by itself to quit).\n")

    # loop until user terminates input
    while True:
        entry = input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

    # Write lines to file with preper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print('Done')


if __name__ == '__main__':
    main()
