#!/usr/bin/env python3
"""Defines a func that safely get a value from a dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """ Returns value from dictionary. """
    if key in dct:
        return dct[key]
    else:
        return default
