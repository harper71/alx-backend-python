#!/usr/bin/env python3
"""
this returns 10 random numbers
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns a list of random number
    from generator

    Returns:
        List[float]: random float numbers
    """
    task1 = [_ async for _ in async_generator()]
    return task1
