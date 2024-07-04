#!/usr/bin/env python3
"""
This module provides a function `safe_first_element` that safely
returns the first element of a sequence or None if the sequence is empty.
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence or None if the
    sequence is empty.

    Args:
        lst: A sequence of any type.

    Returns:
        The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
