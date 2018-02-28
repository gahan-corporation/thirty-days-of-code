#!/usr/bin/env python3
"""HackerRank Day 10."""


def decimal_to_binary(quotient, binary):
    """Convert decimal to binary."""
    print(quotient)
    new_quotient = quotient // 2
    remainder = quotient % 2
    binary.append(str(int(remainder)))
    if new_quotient > 0.9:
        return decimal_to_binary(new_quotient, binary)
    else:
        binary = ''.join(binary[::-1])
        return binary


def count_consecutive_ones(binary):
    """Count consecutive ones."""
    print(binary)
    count = 1

    for i in range(1, len(binary)):
        if binary[i] == 0:
            continue

        if binary[i-1] == binary[i]:
            count = count + 1
    print(count)


[count_consecutive_ones(decimal_to_binary(i, [])) for i in range(1, 512)]
