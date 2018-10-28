# Python dictionary -> hash tables.
# hash collisions -> keys have same hash value
# open addressing -> With this method a hash collision is resolved by probing, 
# or searching through alternate locations in the array (the probe sequence) until either the target record is found, 
# or an unused array slot is found, which indicates that there is no such key in the table.
class HashTable(object):
    def __init__(self):
        self.size = 256 #initial size
        self.buckets = [None] * self.size

    def hash(self, key):
        hash_sum = 0
        for ch in str(key):
            hash_sum += ord(ch)
        return hash_sum % self.size

    def insert(self, key, value):
        hash_key = self.hash(key)
        if not self.buckets[hash_key]:
            self.buckets[hash_key] = [[key, value]]
            return True
        else:
            key_exist = False
            for li in self.buckets[hash_key]:
                if li[0] == key:#if find key
                    li[1] = value #update value
                    key_exist = True
            if not key_exist:
                self.buckets[hash_key].append([key, value])

    def search(self, key):
        hash_key = self.hash(key)
        if self.buckets[hash_key]:
            for li in self.buckets[hash_key]:
                if li[0] == key:
                    return li[1]
        return None

    def delete(self, key):
        hash_key = self.hash(key)
        if not self.buckets[hash_key]:
            return False
        for i in range(len(self.buckets[hash_key])):
            if self.buckets[hash_key][i][0] == key:
                self.buckets[hash_key].pop(i)
                return True
        return False
            