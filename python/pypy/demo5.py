# -*- coding: utf-8 -*-

"""
Python:
--- 0.477239131927 seconds ---

PyPy:
--- 0.0114500522614 seconds ---
"""

import time


def main():
    i = 10000000
    while i:
        i -= 1

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))