#!/usr/bin/env python3
"""
tthe annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    the annotated function
    """
    return (k, float(v ** 2))
