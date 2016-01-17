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


def f3(n):
    """
    递归法:最多一次跳 2 级, for方法
    :param n:
    :return:
    """
    if n <= 2:
        return n
    rs = [0, 1]
    for i in xrange(n):
        x = rs[1]
        rs[1] += rs[0]
        rs[0] = x

    return rs[1]


if __name__ == '__main__':
    print 'f1:', f1(6)
    print 'f1:', f1(5)
    print 'f2:', f2(4)
    print 'f3:', f3(6)
