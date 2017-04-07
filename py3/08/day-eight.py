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
        "Billy 3107281113",
        "Brad 8182229181",
        "Johnny 2021849131",
        "Angelina 4241982193",
        "Jennifer 2918881111",
        "Brad",
        "Jennifer",
        "Billy",
    ] 

phone_book = {}

for si in s:
    sa = si.split(" ")
    if len(sa) > 1:
        phone_book.update({sa[0]:sa[1]})
    print(phone_book)
sb = [i for i in reversed(sa)]
sa = ' '.join(sb)
print(sa)
