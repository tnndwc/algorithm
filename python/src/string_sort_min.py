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


def quick_select(s, k, left, right):
    """
    寻找最小的K个数
    :param s:
    :param k: k个数
    :param left:
    :param right:
    :return:
    """
    if left <= right:
        pivot = median3(s, left, right)
        i = left
        j = right - 1

        while True:
            while s[++i] < pivot:
                pass

            while s[--j] > pivot:
                pass

            if i < j:
                swap(s, i, j)
            else:
                break

        swap(s, i, right - 1)

        if k <= i:
            quick_select(s, k, left, i - 1)
        elif k > i + 1:
            quick_select(s, k, i + 1, right)


def swap(s, i, j):
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp


