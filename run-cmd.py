#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   run-cmd.py
# Purpose:    
#
# Author:      Ke Wang
#
# Created:     2019-11-01
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import subprocess

def run_command(command, wait=False):

    try:
        if (wait):

            p = subprocess.Popen(
                [command],
                stdout = subprocess.PIPE,
                shell = True)
            p.wait()
        else:
            p = subprocess.Popen(
                [command],
                shell = True,
                stdin = None, stdout = None, stderr = None, close_fds = True)

        (result, error) = p.communicate()

    except subprocess.CalledProcessError as e:
        sys.stderr.write(
            "common::run_command() : [ERROR]: output = %s, error code = %s\n"
            % (e.output, e.returncode))

    return result

def main():
    run_command('ls -l /tmp')

if __name__ == '__main__':
    main()
