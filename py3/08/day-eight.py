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
        "Joseph",
    ] 

phone_book = {}

for si in s:
    sa = si.split(" ")
    if len(sa) > 1:
        phone_book.update({sa[0]:sa[1]})
    if len(sa) == 1:
        if phone_book.get(sa[0]) != None:
            print("{0}={1}".format(sa[0],phone_book.get(sa[0])))
        else:
            print("Not found")
