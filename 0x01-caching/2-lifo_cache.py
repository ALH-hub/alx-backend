#!/usr/bin/env python3
"""lifo caching algorithm"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """lifo cache class implementation"""
    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """insert into lifo cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.queue.pop()
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)

    def get(self, key):
        """retrieve item from the cache"""
        return self.cache_data.get(key, None)
