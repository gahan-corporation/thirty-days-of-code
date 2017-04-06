#!/usr/bin/env python3

from threading import Timer

i = 4
d = 4.0
s = "Run's house "

a = Timer(1, print, ["That weren't no input."])
a.start()
j = input()
a.cancel()

b = Timer(1, print, ["That weren't no input."])
b.start()
e = input()
b.cancel()

c = Timer(1, print, ["That weren't no input."])
c.start()
t = input()
c.cancel()

try: 
    k = i + int(j)
    print(k)
except Exception as exc:
    print(exc)

try:
    e = d + float(f)
    print(e)
except Exception as exc:
    print(exc)

try:
    u = "{0}{1}".format(s, t)
    print(u)
except Exception as exc:
    print(exc)
