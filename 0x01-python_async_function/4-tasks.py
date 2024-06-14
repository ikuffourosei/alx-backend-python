#!/usr/bin/env python3
"""wait_random_task"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a funcion that spawns wait_random n times
    with the specified max_delay
    """
    batch = [task_wait_random(max_delay) for i in range(n)]
    result = await asyncio.gather(*batch)
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    return result
