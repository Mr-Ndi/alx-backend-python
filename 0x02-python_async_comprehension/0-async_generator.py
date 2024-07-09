#!/usr/bin/env python3

"""
    A sample module.
"""
import asyncio
from random import uniform
"""
importing neccesary ribraly
"""


async def async_generator():
    """
        This is the function to be based on.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
