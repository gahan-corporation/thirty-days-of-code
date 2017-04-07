#!/usr/bin/env python3

import select
import sys

s = []
t = select.select([sys.stdin], [], [], 1)

try:
    t = int(n[0][0].readline())

    for i in range(0,t):
        print(i) 
except:
    t = 2

    for i in range(0,t):
        if i % 2 == 1:
            s.append("There's no replacement for displacement.")
        else:
            s.append("I firmly believe that any man's finest hour, the greatest fulfillment of all that he holds dear, is that moment when he has worked his heart out in a good cause and lies exhausted on the field of battle - victorious.")

for i in range(0, len(s)):
    s_odd = []
    s_even = []

    for k,v in enumerate(s[i]):
        if k % 2 == 0:
            s_even.append(v)
        else:
            s_odd.append(v)

    s_even = ''.join(s_even);
    s_odd = ''.join(s_odd);

    print("{0} {1}\n".format(s_even, s_odd))
