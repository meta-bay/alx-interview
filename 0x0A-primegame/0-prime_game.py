#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Prime game function """
    def prime_number(n):
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if (prime[p]):
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        return [p for p in range(2, n + 1) if prime[p]]

    def play_round(n):
        turn = 0
        primes = prime_number(n)
        remaining = set(range(1, n + 1))

        while primes:
            prime = primes[0]
            multiples = set(range(prime, n + 1, prime))
            remaining -= multiples
            primes = [p for p in primes if p in remaining]
            turn = 1 - turn
        return 'Ben' if turn == 0 else 'Maria'

    if x < 1 or not nums:
        return None

    ben_wins = 0
    maria_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
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
