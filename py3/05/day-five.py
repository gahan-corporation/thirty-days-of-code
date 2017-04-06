#!/usr/bin/env python3

import select
import sys

n = select.select([sys.stdin], [], [], 1)

try:
    n = int(n[0][0].readline())

    for i in range(1,11):
        print("{0} x {1} = {2}".format(n,i,n*i))
except:
    n = 50

    for i in range(1,11):
        print("{0} x {1} = {2}".format(n,i,n*i))
