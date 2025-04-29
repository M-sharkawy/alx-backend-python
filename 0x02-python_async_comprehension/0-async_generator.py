#!/usr/bin/env python3
"""model for Async Generator"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """function  yield a random number between 0 and 10"""
    for num in range(1, 11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
