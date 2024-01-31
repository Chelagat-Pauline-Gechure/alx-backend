#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from BaseCaching and
is a caching system:

You must use self.cache_data - dictionary from the parent class
BaseCaching
You can overload def __init__(self): but don’t forget to call
the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for
the key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following
by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and implements a caching system
    using FIFO eviction policy
    """

    def __init__(self):
        """Constructor for FIFOCache class
        Initializes the FIFOCache instance by calling the constructor
        of the parent class BaseCaching.
        """
        super().__init__()

    def put(self, key, item):
        """Inserts a key-value pair into the cache

        Args:
            key: The key to be inserted into the cache.
            item: The value corresponding to the key to be stored in the cache.

        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data exceeds BaseCaching.MAX_ITEMS
        the first item put in cache (FIFO algorithm) is discarded, & a message
        indicating the discarded key is printed.
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

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
