#!/usr/bin/env python3

import select
import sys

t = select.select([sys.stdin], [], [], 1)

try:
    t = int(t[0][0].readline())

    u = select.select([sys.stdin], [], [], 1)
    s = u[0][0].readline()
        
except Exception as e:
    print(e)
    t = 2
    s = "0 9 8 1 3 7 3 9 1"

sa = s.split(" ")
print(sa)
