#!/usr/bin/bash

"""
    Annoting the function as asked
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
        A function that takes an iterable of sequences and returns
        a list of tuples with each sequence and its length.
    '''
    return [(i, len(i)) for i in lst]
