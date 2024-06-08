#!/usr/bin/env python3
''' function "sum_mixed"_list which takes a list
"mxd_lst" of integers and floats and returns their sum as a float.'''


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of the mixed list"""
    sum: float = 0
    for num in mxd_list:
        sum += num
    return float(sum)
