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
