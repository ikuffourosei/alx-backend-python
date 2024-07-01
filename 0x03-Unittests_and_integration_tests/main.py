#!/usr/bin/env python3
from utils import access_nested_map


nested_map = {"a": {"b": 2}}

path = ('a','b', 'c')
nest = access_nested_map(nested_map, path)
print(nest)
