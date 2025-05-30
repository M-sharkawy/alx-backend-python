#!/usr/bin/env python3
"""model to """
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an Async task for wait_random."""
    Task = asyncio.create_task(wait_random(max_delay))
    return Task
