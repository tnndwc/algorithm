# -*- coding: utf-8 -*-

"""
求最大「连续子数组」的和
"""


def sub_array_sum(num_arr):
    """
    for 循环实现
    :param num_arr:
    :return: 最大的和
    """
    rs = 0
    arr_len = len(num_arr)
    for m in xrange(arr_len):
        for i in xrange(m, arr_len):

            sum = num_arr[i]
            for n in xrange(i + 1, arr_len):
                sum += num_arr[n]
                if sum > rs:
                    rs = sum
    return rs


def dynamic_sum(num_arr):
    """
    利用动态规划方法
    :param num_arr:
    :return: 最大的和
    """
    curr_sum = 0
    max_sum = 0
    for n in xrange(len(num_arr)):
        if curr_sum >= 0:
            curr_sum += num_arr[n]
        else:
            curr_sum = num_arr[n]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum