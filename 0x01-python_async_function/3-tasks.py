#!/usr/bin/env python3
""" Tasks """

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task for wait_random"""

    return asyncio.create_task(wait_random(max_delay))
