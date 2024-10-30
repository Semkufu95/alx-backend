#!/usr/bin/env python3
'''
A LIFOCache module
'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    A class that inherits from BaseCaching class
    It implements the LIFO algorithm
    '''
    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.cache = []  # A list of cached data.

    def put(self, key, item):
        '''
        Assign item to cache_data
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            # remove key from cache if it already exists
            self.cache.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.cache.pop()
            del self.cache_data[last_key]  # delete the last item
            print(f'DISCARD: {last_key}')

        self.cache_data[key] = item
        self.cache.append(key)

    def get(self, key):
        '''
        Retrieves value of self.cache_data linked to key
        '''
        return self.cache_data.get(key, None)
