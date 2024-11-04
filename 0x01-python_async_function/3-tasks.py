#!/usr/bin/env python3
"""wait a random task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio task for wait_random.

    Args:
        max_delay (int): maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio task object for wait_random.
    """
    task = asyncio.create_task(wait_random(max_delay))
    
    return task
