#!/usr/bin/env python

import select
import sys

i = 4
d = 4.0
s = "Run's house "

j = select.select([sys.stdin], [], [], 1)

if len(j[0]) > 0:
    j = j[0]

    k = i + j

    print(k)
else:
    print("There weren't no input.")
