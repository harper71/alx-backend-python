#!/usr/bin/env python3

"""this measures the total time it takes
to run a asyncronou function stacked four times
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures total time it takes for
    async_comprehension to run 4 times

    Returns:
        float: total time taken
    """

    startTime: float = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    endTime: float = time.time()
    totalTime = endTime - startTime

    return totalTime
