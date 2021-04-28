"""
380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element 
exists when this method is called). Each element must have the same probability of being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
"""

"""
Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""

import random
import math

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.val_to_index = {}
        self.index_to_val = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_index:
            return False

        self.count += 1
        self.index_to_val[self.count] = val
        self.val_to_index[val] = self.count
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_index:
            return False

        last_val = self.index_to_val[self.count]
        index_of_cur_val = self.val_to_index[val]
        self.index_to_val[index_of_cur_val] = last_val
        self.val_to_index[last_val] = index_of_cur_val

        del self.val_to_index[val]
        del self.index_to_val[self.count]
        self.count -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = math.ceil(self.count * random.random())
        return self.index_to_val[index]


r = RandomizedSet()
print(r.insert(55))
print(r.insert(66))
print(r.insert(77))
print(r.getRandom())
print(r.insert(55))
print(r.insert(66))
print(r.remove(66))
print(r.getRandom())
print(r.insert(66))
print(r.getRandom())


'''
Another implementation using Array and Map:

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_index = {}
        self.array = []
        self.count = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_index:
            return False
        
        self.array.append(val)
        self.val_to_index[val] = self.count
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        lastVal = self.array[-1]
        self.val_to_index[lastVal] = index
        self.array[index] = lastVal

        self.array.pop()
        del self.val_to_index[val]
        self.count -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = math.floor(self.count * random.random())
        return self.array[index]
'''
