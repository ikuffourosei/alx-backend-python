#!/usr/bin/env python3
"""A function"""


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
def task_wait_random(max_delay: int):
    """Returns Asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
