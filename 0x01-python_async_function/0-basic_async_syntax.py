#!/usr/bin/env python3
"""
Module that waits for a random delay between 0 and max_delay.
"""

import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """ Return a randomly generated float """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
