#!/usr/bin/env python3
"""Annotate the below function’s parameters
and return values with the appropriate typesr"""
from typing import List, Tuple, Sequence, Iterable, Callable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
