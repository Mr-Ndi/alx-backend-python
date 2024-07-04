#!/usr/bin/bash

"""
    Annoting the function as asked
"""

from typing import Sequence, Any, Union

NoneType = type(None)


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Documenting the asked function"""
    if lst:
        return lst[0]
    else:
        return None
