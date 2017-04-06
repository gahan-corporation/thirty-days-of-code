#!/usr/bin/env python3

import select
import sys

i = 4
d = 4.0
s = "Run's house "

j = select.select([sys.stdin], [], [], 1)
e = select.select([sys.stdin], [], [], 1)
t = select.select([sys.stdin], [], [], 1)

try:
    k = i + int(j[0][0].readline())
    print(k)

    f = d + float(e[0][0].readline())
    print(f)

    s = "{0}{1}".format(s, t[0][0].readline())
    print(s)
except Exception as exc:
    print(exc)

