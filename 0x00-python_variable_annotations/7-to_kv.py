#!/usr/bin/env python3
""" a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element
is the square of the int/float v and should be annotated as a float.
"""


def to_kv(k: str, v: int, float) -> float:
    """Returns a tuple"""
    result: tuple = (k, v ** 2)
    return result
