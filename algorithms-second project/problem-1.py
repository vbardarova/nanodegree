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


print("***Cache with Capacity 0 Test***")
empty_cache = LRU_Cache(0)
print("Add (1,1) to Cache")
empty_cache.set(1,1)
print("Get value at key 1:",empty_cache.get(1))

print("***Cache with Capacity 1 Test***")
one_cache = LRU_Cache(1)
print("Add (1,1) to Cache")
one_cache.set(1,1)
print("Get value at key 1:",one_cache.get(1))
one_cache.set(2,2)
print("Get value at key 1:",one_cache.get(1))
print("Get value at key 2:",one_cache.get(2))
print("***Cache with Capacity 5 Test***")


print("***Cache with Capacity 5 Test***")
five_cache = LRU_Cache(5)
print("Add (1,1) to Cache")
five_cache.set(1, 1);
five_cache.set(2, 2);
five_cache.set(3, 3);
five_cache.set(4, 4);

print("Contents of Cache:",five_cache.cache)
print("Get value at key 1:",five_cache.get(1))  # returns 1
print("Get value at key 3:",four_cache.get(2))
print("Get value at key 3:",four_cache.get(9))
five_cache.set(5, 5) 
five_cache.set(6, 6)
print("Get value at key 3:",four_cache.get(2)) # returns 2
print("Get value at key 3:",four_cache.get(9)) # returns -1 because 9 is not present in the cache
print("Get value at key 3:",four_cache.get(3)) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry




