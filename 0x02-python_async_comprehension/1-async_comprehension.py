#!/usr/bin/env python3
"""
Use async_generator from the previous task and then write a coroutine called
async_comprehension that takes no arguments.
"""

from typing import List


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing over async_generator
    """

    async_generator = __import__('0-async_generator').async_generator
    return [number async for number in async_generator()]
