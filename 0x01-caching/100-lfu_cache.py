#!/usr/bin/python3
"""lfu cache algorithm"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """lfu cache class"""

    def __init__(self):
        """constructor of the class"""
        self.queue = []
        self.freq = {}
        super().__init__()

    def put(self, key, item):
        """insert into the lfu cache"""
        if key and item:
            if (len(self.queue) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                delete = self.queue.pop(0)
                self.freq.pop(delete)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

            if self.cache_data.get(key):
                self.queue.remove(key)
                self.freq[key] += 1
            else:
                self.freq[key] = 0

            insert_index = 0
            while (insert_index < len(self.queue) and
                   not self.freq[self.queue[insert_index]]):
                insert_index += 1
            self.queue.insert(insert_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """get from the lfu cache"""
        if self.cache_data.get(key):
            self.freq[key] += 1
            if self.queue.index(key) + 1 != len(self.queue):
                while (self.queue.index(key) + 1 < len(self.queue) and
                       self.freq[key] >=
                       self.freq[self.queue[self.queue.index(key) + 1]]):
                    self.queue.insert(self.queue.index(key) + 1,
                                      self.queue.pop(self.queue.index(key)))
        return self.cache_data.get(key)