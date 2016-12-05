#!/usr/bin/env python

from __future__ import print_function
import time
import sys

# Get current date and time

var = 1

while var == 1 :
 loctime = time.strftime("%H:%M:%S")
 print(loctime)
 time.sleep(1)

