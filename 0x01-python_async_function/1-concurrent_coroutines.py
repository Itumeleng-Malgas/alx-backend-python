#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
async def wait_n(n, max_delay):
    """ Execute multiple coroutines concurrently """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
