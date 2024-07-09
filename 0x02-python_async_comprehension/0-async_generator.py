#!/usr/bin/env python3

"""
    A sample module.
"""
import asyncio
import random
"""
importing neccesary ribraly
"""


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
