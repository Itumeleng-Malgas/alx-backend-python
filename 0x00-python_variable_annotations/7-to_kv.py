#!/usr/bin/env python3
"""Function that converts a variable to a KV pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Python variable to a KV pair."""
    return k, v ** 2
