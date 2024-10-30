#!/usr/bin/env python3
"""
FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache, a class that inherits from BaseCaching
    and is a caching system
    '''
    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.cache = []

    def put(self, key, item):
        '''
        Assign an item to cache
        '''
        if key is None and item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # remove and print first item
            first_key = self.cache.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.cache.append(key)

    def get(self, key):
        '''
        Return value of self.cache_data linked to key
        '''
        return self.cache_data.get(key, None)
