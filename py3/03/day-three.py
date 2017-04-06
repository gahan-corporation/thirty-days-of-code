#!/usr/bin/env python3

import select
import sys

n = select.select([sys.stdin], [], [], 1)

try:
    n = int(n[0][0].readline())
except Exception as e:
    n = 24

if n % 2 == 1:
    print("Weird")
elif (n % 2 == 0) and (n > 1 and n < 6):
    print("Not Weird")
elif n % 2 == 0 and (n > 5 and n < 21):
    print("Weird")
else:
    print("Not Weird")
