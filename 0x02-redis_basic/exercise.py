#!/usr/bin/env python3

import redis
import uuid
from typing import Union 
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
