#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   yaml-op.py
# Purpose:    
# Required:    PyYAML module
# Author:      Ke Wang
#
# Created:     2019-10-14
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# test_data.yaml
# cases:
#  - case_1
#  - case_2
#  - case_3
#  - case_4

import sys
import os
import yaml

def main():
    work_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    with open('%s/test_data.yaml' % work_path) as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        for case in data['cases']:
            case = case + '()'
            #  eval(case)

if __name__ == '__main__':
    main()
