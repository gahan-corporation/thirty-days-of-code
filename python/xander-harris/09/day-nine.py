#!/usr/bin/env python3
"""HackerRank Day 9."""

import select
import sys

t = select.select([sys.stdin], [], [], 1)

try:
    t = int(t[0][0].readline())

except Exception as e:
    print(e)
    t = 3


def factorial(n):
    """Compute a factorial."""
    if n == 1:
        return n

    f = factorial(n-1) * n
    return f


m = factorial(t)
print(m)
