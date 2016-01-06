# -*- coding: utf-8 -*-

"""
寻找最小的K个数
"""


def median3(s, left, right):
    """
    取列表中3个数字的中值
    :param s:
    :param left:
    :param right:
    :return:
    """
    m = (left + right) >> 1
    if s[left] > s[m]:
        tmp = s[m]
        s[m] = s[left]
        s[left] = tmp

    if s[m] > s[right]:
        tmp = s[m]
        s[m] = s[right]
        s[right] = tmp

    if s[left] > s[m]:
        tmp = s[m]
        s[m] = s[left]
        s[left] = tmp

    return s[m]

