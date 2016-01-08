# -*- coding: utf-8 -*-

"""
插入排序
注意与冒泡排序区分
"""
from utils import swap


def insert_sort(s):
    list_size = len(s)
    for i in xrange(list_size):
        j = i - 1
        temp = s[i]
        while j >= 0 and temp < s[j]:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = temp

