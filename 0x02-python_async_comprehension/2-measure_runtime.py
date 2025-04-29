#!/usr/bin/env python3
"""
model to measure the Run time
for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measures the Runtime for four parallel comprehensions"""
    start_time = time.time()
    tasks = await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension())
    return (time.time() - start_time)
