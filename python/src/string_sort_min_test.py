# coding=utf-8

from string_sort_min import median3
from string_sort_min import quick_select

num_list = [19, 100, 3, 0, 2]

print num_list[0]
print (0 + len(num_list)) >> 1
print median3(num_list, 0, len(num_list) - 1)

print 'sort list:'
quick_select(num_list, 4, 0, len(num_list) - 1)
print ','.join(str(n) for n in num_list)
