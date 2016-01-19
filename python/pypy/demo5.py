# -*- coding: utf-8 -*-

"""
Python:
--- 0.533946037292 seconds ---

PyPy:
--- 0.00886797904968 seconds ---
"""

import time


def main():
    i = 10000000
    while i:
        i -= 1
        if i < 100:
            break
    return i

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))