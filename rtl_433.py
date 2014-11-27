#!/bin/env python

import subprocess

process = subprocess.Popen(['rtl_433', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
  print('waiting for data')
  print(process.stderr.readline())
