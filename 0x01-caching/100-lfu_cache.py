#!/usr/bin/env python3
'''
A module LFUCache
'''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' Inherits from Base Model
    Uses  last recently used to cache data
    '''
    def __init__(self):
        ''' Initialize
        '''
        super().__init__()
        self.frequency = {}  # Tracks access frequency of each key
        self.cache = []  # A list of cached cache

    def put(self, key, item):
        '''
        Assign a lru cache
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            #  Remove key from cache if already exists
            self.cache_data[key] = item
            self.cache.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key = self.cache.pop()
            del self.cache_data[lfu_key]
            print(f"DISCARD: {lfu_key}")

        self.cache_data[key] = item  # Add item to cache
        self.cache.append(key)  # update cache

    def get(self, key):
        ''' retrieves the keys in self.cache_data
        '''
        if key is None or key not in self.cache_data:
            return None

        # move accessed key to the end to mark as recent used
        self.cache.remove(key)
        self.cache.append(key)

        return self.cache_data[key]
