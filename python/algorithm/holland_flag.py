# -*- coding: utf-8 -*-

"""
荷兰国旗问题
"""


def holland(ball):
    """
    将不同的小球乱序排列,通过两两交换任意两个球,使得从左到右的球依次是红球\白球\篮球

    每种颜色的球用数字表示:
    红球:0
    白球:1
    篮球:2
    :param ball:
    :return: 排序好的ball结果集
    """
    ball_size = len(ball)

    # 后指针
    end = ball_size - 1

    if end <= 0:
        return ball

    # 中指针
    current = 1

    # 前指针
    begin = 0

    for n in xrange(ball_size):
        print n

    return ball
