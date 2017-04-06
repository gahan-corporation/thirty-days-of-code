#!/usr/bin/env python3

import select
import sys

n = select.select([sys.stdin], [], [], 1)

try:
    n = int(j[0][0].readline())
except:
    n = 20

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n > 1 and n < 6:
    print("Not Weird")
elif n % 2 == 0 and n > 5 and n < 21: 
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
