#!/usr/bin/env python3

"""
an asynchronous code that takes
a data and awaits for its return
"""
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """async code that waits according to the max_delay

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: the value delay
    """

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
