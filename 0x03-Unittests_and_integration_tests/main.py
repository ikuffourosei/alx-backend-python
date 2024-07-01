#!/usr/bin/env python3
from utils import get_json

test_url="https://jsonplaceholder.typicode.com/todos?userId=2"
get = get_json(test_url)
print(get)
