"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class DoublyLinkedNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return 'Node({})'.format(self.key)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashMap = {}

        self.head = DoublyLinkedNode(-1, -1)
        self.tail = DoublyLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _append(self, node: DoublyLinkedNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _pop(self):
        if self.size <= 0:
            return
        last = self.tail.prev
        self._remove(last)

        del self.hashMap[last.key]
        del last

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1

        node = self.hashMap[key]
        self._remove(node)
        self._append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap and self.size >= self.capacity:
            self._pop()
            self.size -= 1

        node = None
        if key in self.hashMap:
            node = self.hashMap[key]
            node.value = value
            self._remove(node)
        else:
            node = DoublyLinkedNode(key, value)
            self.hashMap[key] = node
            self.size += 1

        self._append(node)


def execute(cmds, inputs):
    res = []
    lruCache = None

    for cmd, input in zip(cmds, inputs):
        if cmd == 'LRUCache':
            capacity = input[0]
            lruCache = LRUCache(capacity)
            ret = None
        elif cmd == 'put':
            key, value = input
            ret = lruCache.put(key, value)
        elif cmd == 'get':
            key = input[0]
            ret = lruCache.get(key)

        res.append(ret)

    print(res)


cmds = ["LRUCache","put","put","put","get"]
inputs = [[2],[1,1],[2,2],[3,3],[1]]
execute(cmds, inputs)

cmds = ["LRUCache","put","put","put","put","get", "get"]
inputs = [[2],[1,1],[2,2],[1,5],[3,3],[2],[1]]
execute(cmds, inputs)

cmds = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
execute(cmds, inputs)

cmds = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get"]
inputs = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4]]
execute(cmds, inputs) # failed testcase
