# -*- coding: utf-8 -*-

from char_all_permutation import cal_recursion, cal_dict_order
from utils import reverse

s = '12345'

# cal_recursion(s, 0, len(s))
print reverse(s, 0, len(s) - 1)
print cal_dict_order(s, len(s))
