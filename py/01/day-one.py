#!/usr/bin/env python

import select
import sys

i = 4
d = 4.0
s = "Run's house "

j, e, t = select.select([sys.stdin], [sys.stdin], [sys.stdin], 1)

k = i + j

print(k)

if len(input_string[0]) > 0:
    print(input_string[0])
else:
    print("There weren't no input.")
