#!/usr/bin/env python

from threading import Timer

i = 4
d = 4.0
s = "Run's house "

a = Timer(1, print, ["That weren't no input."])
a.start()
j = input()
a.cancel()
