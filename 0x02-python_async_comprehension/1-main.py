#!/usr/bin/env python3

import asyncio

wait_random =__import__('0-main').wait_random
waited = asyncio.run(wait_random())

print(waited)

