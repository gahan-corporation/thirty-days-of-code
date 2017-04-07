#!/usr/bin/env python3

import select
import sys

t = select.select([sys.stdin], [], [], 1)

try:
    t = int(t[0][0].readline())

except Exception as e:
    print(e)
    t = 50

