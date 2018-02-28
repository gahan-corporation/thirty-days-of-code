#!/usr/bin/env python3
"""HackerRank Day 10."""


def decimal_to_binary(quotient, binary):
    """Convert decimal to binary."""
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
    count = 1

    for i in range(1, len(binary)):
        if binary[i] == 0:
            continue

        if binary[i-1] == binary[i]:
            count = count + 1
    print(count)


binary_result = decimal_to_binary(13, [])
result = count_consecutive_ones(binary_result)

binary_result = decimal_to_binary(5, [])
result = count_consecutive_ones(binary_result)

binary_result = decimal_to_binary(6, [])
result = count_consecutive_ones(binary_result)
