#!/usr/bin/env python3
'''
Run time for four parallel comprehensions
'''


import asyncio
import time
new_coroutine = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Run time for four parallel comprehensions
    using the async.gather() method
    '''
    starting_time = time.perf_counter()

    await asyncio.gather(
        new_coroutine(),
        new_coroutine(),
        new_coroutine(),
        new_coroutine())
    return time.perf_counter() - starting_time
