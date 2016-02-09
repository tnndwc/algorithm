# -*- coding: utf-8 -*-

"""
荷兰国旗问题
将不同的小球乱序排列,通过两两交换任意两个球,使得从左到右的球依次是红球\白球\篮球
每种颜色的球用数字表示:
红球:0
白球:1
篮球:2
"""

from holland_flag import holland

ball = [1, 0, 2, 1, 1, 2, 1, 0, 2, 1, 2]
print 'ball size = ', len(ball)

print holland(ball)

