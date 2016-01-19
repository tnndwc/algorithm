# -*- coding: utf-8 -*-

"""
Python:
--- 11.3639998436 seconds ---

PyPy:
--- 0.578999996185 seconds ---
"""

import time


def main():
    str1 = ''
    for i in xrange(10000000):
        str1 = "%d %d" % (i, i)
    return str1

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))