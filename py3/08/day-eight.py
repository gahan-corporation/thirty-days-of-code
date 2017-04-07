#!/usr/bin/env python3

import select
import sys

s = []
u = None 
t = select.select([sys.stdin], [], [], 1)

try:
    t = int(t[0][0].readline())

    while u != "":
        u = select.select([sys.stdin], [], [], 1)
        s.append(u[0][0].readline())
        
except Exception as e:
    print(e)
    t = 5
    s = [
        "Billy Bob Thornton 3107281113",
        "Brad Pitt 8182229181",
        "Johnny Lee Miller 2021849131",
        "Angelina Jolie 4241982193",
        "Jennifer Aniston 2918881111",
        "Brad Pitt",
        "Jennifer Aniston",
        "Billy Bob Thornton",
    ] 

for si in s:
    sa = s.split(" ")
    print(sa)
sb = [i for i in reversed(sa)]
sa = ' '.join(sb)
print(sa)
