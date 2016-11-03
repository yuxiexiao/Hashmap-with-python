
class HashTable:
    '''
    Implementation of a fixed-size hash map that associated string
    keys with arbitrary data object references.
    '''

    def __init__(self, size):
        '''
        Initializes a fixed-size hash map that takes strings for keys.
        The number of slots is pre-allocated given the number of objects.
        The hash map is represented as a three dimensional list
        (A list of lists of lists).

        Example format - items of two full hash maps of size 4:
            [[[key1,val1]], [[key2, val2]], [[key3, val3]], [[key4, val4]]]

            [[[keyA,val1], [keyB,val2]], [[keyC, val3]], [[keyD, val4]], []]
        '''

        if size < 1:
            raise ValueError("Capacity of hash map must be greater than 0")

        self.capacity = size
        self.size = 0
        self.items = [[] for slot in range(self.capacity)]

    def set(self, key, value):
        '''
        Stores the given key/value pair in the hash map. Returns a boolean
        value indicating success/failure of the operation.
        Since this is a fixed-size hash map, the function will return False if
        capacity is reached.
        Set() uses chaining to avoid collisions.
        '''

        index = self.getIndex(key)
        found = False
        # check if the key is already in the hash map; if so, update its value
        for item in self.items[index]:
            if item[0] == key:
                item[1] = value
                found = True
                break

        # if the item is not found, add it to the hash map
        if not found:
            if self.size >= self.capacity:
                return False
            self.items[index].append([key, value])
            self.size += 1
        return True

    def get(self, key):
        '''
        Returns the value associated with the given key, or None if the key
        has no value.
        '''
        index = self.getIndex(key)
        for item in self.items[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        '''
        Deletes the value associated with the given key, returning the value
        on success or None if the key has no value.
        '''
        index = self.getIndex(key)
        foundVal = None
        for item in self.items[index]:
            if item[0] == key:
                foundVal = item[1]
                self.items[index].remove(item)
                self.size -= 1
                break

        return foundVal

    def load(self):
        '''
        Returns a float value representing the load factor.
        '''
        return float(self.size) / float(self.capacity)

    def getIndex(self, key):
        '''
        Dan Bernstein's djb2 hashing algorithm:
        http://www.cse.yorku.ca/~oz/hash.html
        '''
        _hash = 5381
        for i in range(0, len(key)):
            _hash = ((_hash << 5) + _hash) + ord(key[i])

        _hash %= self.capacity
        return _hash


