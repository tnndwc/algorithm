# -*- coding: utf-8 -*-

"""
跳台阶问题
此问题实际上是一个类Fibonacci算法
"""


def f1(n):
    """
    递归法:最多一次跳 2 级
    :param n:
    :return:
    """

    if n <= 2:
        # 返回n种跳法
        return n
    return f1(n - 1) + f1(n - 2)


def f2(n):
    """
    递归法:最多一次跳 3 级
    :param n:
    :return:
    """

    if n <= 3:
        return 2 ** (n -1)
    return f2(n - 1) + f2(n - 2) + f2(n - 3)


if __name__ == '__main__':
    print 'f1:', f1(3)
    print 'f2:', f2(4)
