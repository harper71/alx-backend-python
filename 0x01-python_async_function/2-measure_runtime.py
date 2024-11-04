#!/usr/bin/env python3
"""checks time taken for
the code to run
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures time
    """
    start_time: float = time.time()
    
    asyncio.run(wait_n(n, max_delay))
    
    end_time: float = time.time()
    total_time = end_time - start_time
    return (total_time / n)
