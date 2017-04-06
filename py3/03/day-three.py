#!/usr/bin/env python3

import select
import sys

n = select.select([sys.stdin], [], [], 1)

try:
    n = int(j[0][0].readline())
except:
    n = 20
