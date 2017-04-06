#!/usr/bin/env python3

import sys


n = int(input().strip())

for i in range(1,11):
    print("{0} x {1} = {2}".format(n,i,n*i))

