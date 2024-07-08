#!/usr/bin/env python3
'''
returnog the time takne to run
'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''taking the max_delay and n to retun the
    runtime of wait_n
    '''
    a = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    delay = (time.perf_counter() - a) / n
    return delay
