#!/usr/bin/env python3

import select
import sys

s = []
u = None 
t = select.select([sys.stdin], [], [], 1)

try:
    t = int(t[0][0].readline())

    u = select.select([sys.stdin], [], [], 1)
    s = u[0][0].readlines()
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
        name=sa[0].strip()
        number=sa[1].strip()
        phone_book.update({name:number})
    if len(sa) == 1:
        search=sa[0].strip()
        if phone_book.get(search) != None:
            print("{0}={1}".format(search,phone_book.get(search)))
        else:
            print("Not found")
