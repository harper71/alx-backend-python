#!/usr/bin/env python3
"""
This module contains a function that runs
multiple coroutines concurrently
and returns a list of their results.
"""
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random 'n' times with the specified 'max_delay' and return a list of all the delays.
    
    Args:
        n (int): Number of times to run wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: List of delays, sorted in ascending order.
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)] 

    listOfDelay = await asyncio.gather(*tasks)

    listOfDelay.sort()

    return listOfDelay
