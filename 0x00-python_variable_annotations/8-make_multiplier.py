#!/usr/bin/env python3
"""a type-annotated function make_multiplier
that takes a float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
