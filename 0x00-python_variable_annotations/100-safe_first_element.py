#!/usr/bin/env python3
"""
This module provides a function `safely_get_value` that returns
the value for a given key from a dictionary if the key exists,
otherwise returns a default value.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    Returns the value for a given key from a dictionary
    if the key exists, otherwise returns a default value.

    Args:
        dct: A dictionary from which to retrieve the value.
        key: The key to look for in the dictionary.
        default: The default value to return if the key is not found.

    Returns:
        The value associated with the key in the dictionary or the
        default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
