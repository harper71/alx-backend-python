#!/usr/bin/env python3
"""Module that contains a type-annotated function zoom_array
that takes a tuple of integers and returns a tuple of integers
with a factor of 2 or 3.0.

"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Change the annotation for 1st and return the type
        to Tuple
        to indicate that the function accepts and
        returns a tuple of any type.
    """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
