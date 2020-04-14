import collections


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self._capacity = capacity
        self._cache = collections.OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        try:
            value = self._cache.pop(key)
            self._cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        try:
            self._cache.pop(key)
        except KeyError:

            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)

        self._cache[key] = value


# tests
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
