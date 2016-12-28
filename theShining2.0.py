#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys

def delay_print(s):
  for c in s:
    sys.stdout.write( '%s' % c )
    sys.stdout.flush()
    time.sleep(0.10)

count = input("How crazy are you? ")

while count !=0:
  delay_print("All work and no play makes Jack a dull boy." + "\n")
  count -= 1 

sys.exit()
