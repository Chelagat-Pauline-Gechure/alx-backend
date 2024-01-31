#!/usr/bin/env python3
"""Create a class BasicCache that inherits from BaseCaching &
is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching
    """

    def __init__(self):
        """Constructor for BasicCache class
        Initializes the BasicCache instance by calling the constructor of the
        parent class BaseCaching.
        """
        super().__init__()

    def put(self, key, item):
        """Inserts a key-value pair into the cache

        Args:
            key: The key to be inserted into the cache.
            item: The value corresponding to the key to be stored in the cache.

        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value associated with the given key from the cache

        Args:
            key: The key for which the value needs to be retrieved.

        Returns:
            The value associated with the given key if the key is present in
            the cache, else returns None.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
