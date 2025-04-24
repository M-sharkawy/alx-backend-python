#!/usr/bin/env python3
"""duck-typed annotations the below function"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck-typed annotations the below function"""
    if lst:
        return lst[0]
    else:
        return None
