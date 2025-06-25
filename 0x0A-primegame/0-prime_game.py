#!/usr/bin/python3
"""Prime game module"""

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    n = max(nums)
    sieve = [True for _ in range(n + 1)]
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if sieve[i]:
            count += 1
        primes_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if primes_count[num] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
