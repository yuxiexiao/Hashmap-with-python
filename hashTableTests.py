import unittest
import hashTable


class TestHashTable(unittest.TestCase):
    '''
    Tests for the fixed-size HashTable class
    '''

    def testInitilization(self):
        # check that initializing a hashmap of size < 1 raises an error
        self.assertRaises(ValueError, hashTable.HashTable, 0)
        self.assertRaises(ValueError, hashTable.HashTable, -10)

        # checks initial properties
        testTable = hashTable.HashTable(5)
        self.assertEqual(testTable.size, 0)
        self.assertEqual(testTable.capacity, 5)
        self.assertEqual(testTable.items, [[], [], [], [], []])

    def testGetSet(self):
        testTable = hashTable.HashTable(10)

        # fill with the keys and values: ['a',0], ['b', 1], ['c', 2], ['d', 3]
        for i, char in enumerate("abcd"):
            testTable.set(char, i)

        # check correct size after filling
        self.assertEqual(testTable.size, 4)
        # check that get returns correct value
        self.assertEqual(testTable.get("a"), 0)
        self.assertEqual(testTable.get("b"), 1)
        self.assertEqual(testTable.get("c"), 2)
        self.assertEqual(testTable.get("d"), 3)

        # check that updating a key changes its value, but not the table size
        testTable.set("a", 99)
        self.assertEqual(testTable.get("a"), 99)
        self.assertEqual(testTable.size, 4)

        # check that set works when the value is an arbitrary data object ref.
        testTable.set("MX", "Michelle!")
        self.assertEqual(testTable.size, 5)
        self.assertEqual(testTable.get("MX"), "Michelle!")

        # test that set returns true on success
        self.assertTrue(testTable.set("GD", "Grace!"))
        self.assertEqual(testTable.get("GD"), "Grace!")

        # test that getting a key not in the table returns None
        self.assertEqual(testTable.get("pants"), None)

    def testFullCapacity(self):
        testTable = hashTable.HashTable(5)

        testTable.set("My", 0)
        testTable.set("Socks", 1)
        testTable.set("Are", 2)
        testTable.set("Really", 3)
        testTable.set("Red", 4)

        # Assert that setting a key/val pair in a full table returns False
        self.assertEqual(testTable.size, 5)
        self.assertFalse(testTable.set("Today", 5))
        self.assertEqual(testTable.get("Today"), None)

        # Assert that updating a value in a full table is valid
        testTable.set("Socks", 99)
        self.assertEqual(testTable.get("Socks"), 99)

        # Assert that updating a value does not change the table size
        self.assertEqual(testTable.size, 5)

    def testRemove(self):
        testTable = hashTable.HashTable(10)

        testTable.set("A", "Apple")

        # test that trying to delete a key not in the list returns None
        self.assertEqual(testTable.delete("B"), None)
        self.assertEqual(testTable.size, 1)

        # test that we can not delete a key/value pair by inputing the value
        self.assertEqual(testTable.delete("Apple"), None)
        self.assertEqual(testTable.size, 1)

        # test that delete(key) returns the value and decrements table size
        self.assertEqual(testTable.delete("A"), "Apple")
        self.assertEqual(testTable.size, 0)
        self.assertEqual(testTable.get("A"), None)

        # test that we can still set a key/value after deleting
        testTable.set("B", "Banana")
        self.assertEqual(testTable.size, 1)
        self.assertEqual(testTable.get("B"), "Banana")

    def testLoad(self):
        testTable = hashTable.HashTable(10)

        # check that an empty table has load == 0.0
        self.assertEqual(testTable.load(), 0.0)

        testTable.set("A", 0)
        self.assertEqual(testTable.load(), 0.1)
        testTable.set("B", 1)
        self.assertEqual(testTable.load(), 0.2)
        testTable.set("C", 2)
        self.assertEqual(testTable.load(), 0.3)
        testTable.set("D", 3)
        self.assertEqual(testTable.load(), 0.4)
        testTable.set("E", 4)
        self.assertEqual(testTable.load(), 0.5)

        for i in range(5, 10):
            testTable.set(str(i), i)

        self.assertEqual(testTable.load(), 1.0)

        # check load never goes above 1.0
        testTable.set("Z", 10)
        self.assertEqual(testTable.load(), 1.0)


if __name__ == "__main__":
    unittest.main()























