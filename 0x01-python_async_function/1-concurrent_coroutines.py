#!/usr/bin/env python3
"""model to spawn wait_random n times and return delays"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Run wait_random n times and collect delays in ascending order"""
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        results = await task
        delays.append(results)

    return delays
