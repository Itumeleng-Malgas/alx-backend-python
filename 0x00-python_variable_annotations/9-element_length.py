#!/usr/bin/env python3
"""Defines a function with annotated parameter."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns length of each element"""
    return [(i, len(i)) for i in lst]
