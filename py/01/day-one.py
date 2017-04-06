#!/usr/bin/env python

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
