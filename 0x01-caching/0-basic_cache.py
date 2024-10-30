#!/usr/bin/env python3
"""
Basic cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class that inherits from BaseCaching
    returns value of cache
    """
    def put(self, key, item):
        '''assigns self.cache_data to item value of key
        if key or value is None should not return anything
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Returns the value in self.cache_data linked to key
        '''
        return self.cache_data.get(key, None)
