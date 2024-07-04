#!/usr/bin/env python3
"""Module for converting a key and a numeric value to a tuple.

This module provides a function that takes a string and a
numeric value (int or float), squares the numeric value,
and returns a tuple consisting of the string and the squared value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key and a numeric value into a tuple with the value squared.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value as an integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the square of
        the value as a float.
    """
    return (k, float(v ** 2))
