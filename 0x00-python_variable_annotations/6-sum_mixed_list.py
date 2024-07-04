#!/usr/bin/python3


"""
    annotated function
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    '''
        A function that takes a list of float ans integer and
        returns their sum.
    '''
    return sum(mxd_list)
