# -*- coding: utf-8 -*-

"""
utils
"""


def swap(s, i, j):
    """
    交换列表中的两个元素，无返回值
    :param s:
    :param i:
    :param j:
    :return: 无
    """
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp


def reverse(s, m, n):
    """
    反转s[m..n]之间的数据
    :param s: s是一个字符串
    :param m:
    :param n:
    :return: list的翻转字符串
    """
    if isinstance(s, str):
        s_list = list(s)

    if n > len(s_list) - 1 or m < 0:
        raise IndexError("s index out of range")

    y = (n + m) / 2
    if (n + m) % 2 > 0:
        y += 1

    index = m
    for x in xrange(y):
        tmp = s_list[index]
        s_list[index] = s_list[n - x]
        s_list[n - x] = tmp
        index += 1

    return ''.join(s_list)
