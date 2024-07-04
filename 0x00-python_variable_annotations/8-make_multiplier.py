#!/usr/bin/env python3

"""
    annotated function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        A function that takes a float multiplier as an argument and returns
         a function that multiplies a float by the multiplier.
    '''
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
