#!/usr/bin/env python3
"""Basic cache dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""
    def put(self, key, item):
        """Assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
