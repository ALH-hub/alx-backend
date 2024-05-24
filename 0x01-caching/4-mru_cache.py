#!/usr/bin/env python3
"""most recently used caching algorithm"""
from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """implementing the mru cache class"""
    def __init__(self):
        """class constructure"""
        super().__init__()
        self.queue = []

    def put(self, key: str, item: str) -> None:
        """insert into the mru cache"""
        if key and item:
            self.cache_data[key] = item
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.queue.pop(-2)
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")

    def get(self, key):
        """retrieve item from cache"""
        if key in self.cache_data:
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        else:
            return None
