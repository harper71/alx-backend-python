#!/usr/bin/python3
"""corrects the code"""
from typing import List, Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that takes a list lst as argument
    and returns its first element if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
