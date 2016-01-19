# -*- coding: utf-8 -*-

"""
这个例子主要耗费在for循环中，并不会直接干预即时编译器，所以，
可能比原生的Python更慢！

Python:
('Cost Time:', 0.017775)

PyPy:
('Cost Time:', 0.001686)
"""

import time

start = time.clock()
s = 1
for i in range(1, 100000 + 1):
    s += i
end = time.clock()
print("Cost Time:", end - start)
