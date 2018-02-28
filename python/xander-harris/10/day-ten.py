#!/usr/bin/env python3
"""HackerRank Day 10."""
# n = int(input().strip())
n = 13


def decimal_to_binary(quotient, binary):
    """Convert decimal to binary."""
    new_quotient = quotient // 2
    remainder = quotient % 2
    binary.append(str(int(remainder)))
    if new_quotient > 0.9:
        return decimal_to_binary(new_quotient, binary)
    else:
        binary = len(max(''.join(binary[::-1]).split("0"), key=len))
        return binary


print(decimal_to_binary(n, []))
