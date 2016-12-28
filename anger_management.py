#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys

def delay_print(s):
  for c in s:
    sys.stdout.write( '%s' % c )
    sys.stdout.flush()
    time.sleep(0.10)

count = input("On a scale of 1 to 10, how mad are you? ")

while count !=0:
  delay_print("\n" + "      *       *" + "\n" + "    *   *   *   *" + "\n" + "   *      *     *" + "\n" + "    *          *" + "\n" + "     *        *" + "\n" + "      *      *" + "\n" + "       *    *" + "\n" + "        *  *" + "\n" + "         **" + "\n" + "\n")
  count -= 1

sys.exit()
