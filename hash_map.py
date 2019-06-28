class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def re_hash(old_hash, size):
        return (old_hash + 1) % size

    def __getitem__(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                data = self.data[position]
                break
            else:
                position = self.re_hash(position, len(self.slots))
                if position == start_slot:
                    break
        return data

    def __setitem__(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.re_hash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.re_hash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace


ht = HashTable()
ht[1] = 42
ht[2] = 43
ht[23] = 55
print(ht[1])
print(ht[2])
print(ht[23])
assert 1
