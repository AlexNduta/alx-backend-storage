#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Optional 
"""
    -setup redis for our code
"""

class Cache():
    """ working with redis """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data: Union[str, bytes, int, float]) -> str:
        new_uuid = str(uuid.uuid4())
        self._redis.set(new_uuid, data)

        return new_uuid

    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        value= self._redis.get(key)

        if fn:
            value = fn(value)

    def get_str(self, key: str) -> str:
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        return sef.get(key, fn=int)



cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value


