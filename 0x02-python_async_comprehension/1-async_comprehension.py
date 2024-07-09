#!/usr/bin/env python3
''' this is the continuation to the task one'''


from typing import List
import asyncio
new_task = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''this is an async comprehension'''
    new_list = []

    async for i in new_task():
        new_list.append(i)
    return new_list
