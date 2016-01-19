# -*- coding: utf-8 -*-

"""
200万以内的素数之和
Python:
--- 0.834000110626 seconds ---

PyPy:
--- 0.055999994278 seconds ---
"""
import time
import math


def calc():
    n = 2000000
    prime = [i for i in range(1, n + 1)]
    r = int(math.sqrt(n))
    for j in range(2, r + 1):
        if prime[j - 1] != 0:
            s = j * j
            while s <= n:
                prime[s - 1] = 0
                s += j

    return sum(prime) - 1


start_time = time.time()
print calc()
print("--- %s seconds ---" % (time.time() - start_time))
