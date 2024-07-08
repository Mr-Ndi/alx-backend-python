#!/usr/bin/env python3
''' this is the basic of asynch in python
'''
import asyncio
from random import uniform
'''
this is the definition of the async function the delays random time'''


async def wait_random(max_delay: int = 10) -> float:

    '''
    we used the unifom method to get the random delay
    and we specify the startig point (0) and the endig point (max_delay)
    '''

    new_delay = uniform(0, max_delay)

    await asyncio.sleep(new_delay)
    return new_delay
