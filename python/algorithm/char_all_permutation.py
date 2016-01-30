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


def print_str(strings):
    print ''.join(strings)


def cal_recursion(strings, n_from, n_to):
    recursion(list(strings), n_from, n_to)
