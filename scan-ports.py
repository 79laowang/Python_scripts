#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   scan-ports.py
# Purpose:     Using thread pool scan ports 
#
# Author:      Ke Wang
#
# Created:     2019-11-06
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket
import datetime
import re
from concurrent.futures import ThreadPoolExecutor, wait

DEBUG = False

# 判断ip地址输入是否符合规范
def check_ip(ipAddr):
  compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
  if compile_ip.match(ipAddr):
    return True
  else:
    return False

# 扫描端口程序
def portscan(ip, port):
  try:
    s = socket.socket()
    s.settimeout(0.2)
    s.connect((ip, port))
    openstr = f'[+] {ip} port:{port} open'
    print(openstr)
  except Exception as e:
    if DEBUG is True:
      print(ip + str(port) + str(e))
    else:
      return f'[+] {ip} port:{port} error'
  finally:
    s.close

#主程序,利用ThreadPoolExecutor创建600个线程同时扫描端口
def main():
  while True:
    ip = input("请输入ip地址:")
    if check_ip(ip):
      start_time = datetime.datetime.now()
      executor = ThreadPoolExecutor(max_workers=600)
      t = [executor.submit(portscan, ip, n) for n in range(1, 65536)]
      if wait(t, return_when='ALL_COMPLETED'):
        end_time = datetime.datetime.now()
        print("扫描完成,用时:", (end_time - start_time).seconds)
        break


if __name__ == '__main__':
  main()
