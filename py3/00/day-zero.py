#!/usr/bin/env python

import select
import sys

input_string = select.select([sys.stdin], [], [], 5)

print('Hello, World.')

if len(input_string[0]) > 0:
    print(input_string[0])
else:
    print("There weren't no input.")
