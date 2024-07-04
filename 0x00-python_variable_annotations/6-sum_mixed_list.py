#!/usr/bin/env python3


"""
    annotated function
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        The mixed list of integers and floats to sum.

    Returns:
        float: The sum of the mixed list.
    """
    return sum(mxd_lst)
