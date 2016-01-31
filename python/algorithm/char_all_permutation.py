# -*- coding: utf-8 -*-

"""
字符串全排列
"""

from utils import swap


def recursion(strings, n_from, n_to):
    """
    用递归方法
    :param strings:
    :param n_from:
    :param n_to:
    :return:
    """
    if n_to <= 1:
        return

    if n_from == n_to:
        print_str(strings)
    else:
        for i in xrange(n_from, n_to):
            swap(strings, i, n_from)
            recursion(strings, n_from + 1, n_to)
            swap(strings, i, n_from)


def dict_order(strings, num):
    """
    按照字典顺序全排列
    :param strings:
    :param num:
    :return:
    """
    i = num - 2

    # 从后向前,找到一个 前数<后数的位置i
    while i >= 0 and strings[i] >= strings[i + 1]:
        i -= 1

    if i < 0:
        return

    k = num - 1

    # 从后向前,找到最后一个数要大于strings[i]
    while k > i and strings[k] <= strings[i]:
        k -= 1

    swap(strings, i, k)





def print_str(strings):
    print ''.join(strings)


def cal_recursion(strings, n_from, n_to):
    recursion(list(strings), n_from, n_to)
