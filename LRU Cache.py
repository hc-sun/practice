class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lru:
            return -1
        val = self.lru[key]
        self.lru.move_to_end(key, last=True) #default-true-move key to right end, false-left end
        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lru:
            del self.lru[key]
            self.lru[key] = value
        elif len(self.lru) == self.capacity:
            self.lru.popitem(last=False) #default-true, false-FIFO, true-LIFO
        self.lru[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Least Recently Used (LRU) cache
