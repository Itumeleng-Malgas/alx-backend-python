#!/usr/bin/env python3
""" 4. Tasks """

task_wait_random = __import__('3-tasks').task_wait_random
import asyncio

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines concurrently using task_wait_random """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
