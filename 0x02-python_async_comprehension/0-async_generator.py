#!/usr/bin/env python3
"""
this uses async function
with generator to loop through random
numbers
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """generates a random float number

    Returns:
        AsyncGenerator[float, None]: a generator of random numbers

    Yields:
        Iterator[AsyncGenerator[float, None]]: random float of range(0, 10)
    """

    for _ in range(10):
        newNums: float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield newNums
