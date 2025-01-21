#!/usr/bin/env python3
"""
the annoteted function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    the first function
    """
    def multiplier_function(value: float) -> float:
        """
        builds upon the first function
        """
        return value * multiplier
    return multiplier_function
