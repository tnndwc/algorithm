# -*- coding: utf-8 -*-

"""
Python:
102334155
--- 43.5290000439 seconds ---

PyPy:
102334155
--- 2.43300008774 seconds ---
即时编译对递归进行了加速处理
"""

import time


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

start_time = time.time()
print fib(40)
print("--- %s seconds ---" % (time.time() - start_time))
