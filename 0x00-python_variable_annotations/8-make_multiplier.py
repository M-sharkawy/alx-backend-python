#!/usr/bin/env python3
"""a type-annotated function make_multiplier
that takes a float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier
    that takes a float multiplier"""
    def multiplier_func(x: float) -> float:
        """multiplie float with the multiplier"""
        return x * multiplier
    return multiplier_func
