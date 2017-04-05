#!/usr/bin/env python

import select
import sys

# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = select.select([sys.stdin], [], [], 5)

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
if len(input_string[0]) > 0:
    print(input_string[0])
else:
    print("There weren't no input.")
