#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Prime game function """
    def prime_number(n):
        primes = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def play_round(n):
        primes = prime_number(n)
        if len(primes) % 2 == 0:
            return 'Ben'
        else:
            return 'Maria'

    if x < 1 or not nums:
        return None

    ben_wins = 0
    maria_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_round(n)
            if winner == 'Maria':
                maria_wins += 1
            else:
                ben_wins += 1

    if ben_wins > maria_wins:
        return 'Ben'
    elif maria_wins > ben_wins:
        return 'Maria'
    else:
        return None
