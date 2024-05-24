#!/usr/bin/env python3
"""fifo cache implementation"""
from collections import deque
from typing import Any, Dict, List, Union
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo cache class"""

    def __init__(self):
        """constructore of the class"""
        super().__init__()
        self.queue = deque()
    
    def put(self, key: str, item: str) -> None:
        """insert into the fifo cache"""
        if key and item:
            self.cache_data[key] = item
            if key not in self.queue:
                self.queue.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.queue.popleft()
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
    
    def get(self, key: str) -> Union[Any, None]:
        """get method"""
        return self.cache_data.get(key, None)
