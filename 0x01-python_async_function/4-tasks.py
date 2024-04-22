#!/usr/bin/env python3
""" 4. Task to execute multiple coroutines concurrently """

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines concurrently using task_wait_random """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
