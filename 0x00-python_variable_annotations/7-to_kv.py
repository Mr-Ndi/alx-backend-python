#!/usr/bin/python3


"""
    annotated function
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    '''A function that takes a string and a float or
        integer and returns a tuple.
       The tuple contains the string and the
       square of the number as a float.
    '''
    return (k, (v ** 2))
