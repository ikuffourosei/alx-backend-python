#!/usr/bin/env python3
"""Annotating the function below"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Annotate to display return type'''
    return [(i, len(i)) for i in lst]
