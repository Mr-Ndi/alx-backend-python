#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay = 10):
    max_delay = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    print ("Hello men")
    return max_delay


asyncio.run(wait_random())