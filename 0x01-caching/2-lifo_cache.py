#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from
the parent class BaseCaching
You can overload def __init__(self): but don’t
forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the
item value for the key key.
If key or item is None, this method should not do
anything.
If the number of items in self.cache_data is higher
that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache
(LIFO algorithm)
you must print DISCARD: with the key discarded and
following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in
self.cache_data, return None.
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and implements a caching system using
    LIFO eviction policy
    """

    def __init__(self):
        """Constructor for LIFOCache class
        Initializes the LIFOCache instance by calling the constructor of the
        parent class BaseCaching.
        """
        super().__init__()

    def put(self, key, item):
        """Inserts a key-value pair into the cache

        Args:
            key: The key to be inserted into the cache.
            item: The value corresponding to the key to be stored in the cache.

        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data exceeds
        BaseCaching.MAX_ITEMS,
        the last item put in cache (LIFO algorithm) is discarded, and a message
        indicating the discarded key is printed.
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value associated with the given key from the cache

        Args:
            key: The key for which the value needs to be retrieved.

        Returns:
            The value associated with the given key if key is present in the
            cache, else returns None.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
