# -*- coding: utf-8 -*-

"""
5000万以内的素数之和(简单的数字处理采用即时编译)
Python:
72619548630277
--- 23.4359998703 seconds ---

PyPy:
72619548630277
--- 1.58999991417 seconds ---
"""
import time
import math


def calc():
    n = 50000000
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
