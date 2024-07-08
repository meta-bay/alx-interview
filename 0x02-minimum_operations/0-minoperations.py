#!/usr/bin/python3
"""
0. Minimum Operations
"""
import math


def prime_factors(n):
    """ Gives a list of prime factor of a number """
    factors = []
    # Divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is a prime greater than 2
    if n > 2:
        factors.append(n)

    return factors


def minOperations(n):
    """
    Calculate the minimum number of
    operations needed to obtain n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed,
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0
    if n in [2, 3, 4]:
        return n

    return sum(prime_factors(n))
