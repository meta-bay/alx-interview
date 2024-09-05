#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Prime game function """
    def prime_number(n):
        primes = []
        is_prime = [True for i in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
        return primes

    def play_round(n):
        turn = 0
        primes = prime_number(n)

        while primes:
            prime = primes[0]
            multiples = set(range(prime, n + 1, prime))
            primes = [p for p in primes if p not in multiples]
            turn = 1 - turn
        return 'Ben' if turn == 0 else 'Maria'

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
