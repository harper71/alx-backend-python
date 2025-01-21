#!/usr/bin/env python3
"""
the annotated function
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    the function correction
    """
    return [(i, len(i)) for i in lst]
