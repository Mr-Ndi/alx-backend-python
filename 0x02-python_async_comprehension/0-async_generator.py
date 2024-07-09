#!/usr/bin/env python3
'''
We are going to import the uniforn from random
and import list from typing
'''


import asyncio
from random import uniform


async def async_generator():
    '''
    This is an async generator
    '''
    for a in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
