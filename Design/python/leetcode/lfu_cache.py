"""
460. LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. 
When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. 
For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. 
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
The use counter for a key in the cache is incremented either a get or put operation is called on it.

Example 1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]
Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3

Constraints:
0 <= capacity, key, value <= 10^4
At most 10^5 calls will be made to get and put.

Follow up: Could you do both operations in O(1) time complexity?
"""
from collections import defaultdict


class Node:
    def __init__(self, key=-1, value=-1, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        self.freq = 1

    def __repr__(self) -> str:
        return 'Node({})'.format(self.key)

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def __repr__(self) -> str:
        res = []
        first = self.head.next
        while first:
            res.append('({}, {})'.format(first.key, first.value))
            first = first.next
        return '->'.join(res[:-1])

    def append(self, node: Node) -> None:
        nextnode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextnode
        nextnode.prev = node
        self.count += 1

    def remove(self, node: Node) -> Node:
        if count == 0:
            return node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.count -= 1
        return node

    def pop(self) -> Node:
        node = self.tail.prev
        return self.remove(node)

    def empty(self) -> bool:
        return self.count == 0

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.leastFreq = 1
        self.nodes = {}
        self.frequencies = defaultdict(DLL)

    def _update(self, node) -> None:
        dll = self.frequencies[node.freq]
        _ = dll.remove(node)
        if dll.empty() and node.freq == self.leastFreq:
            self.leastFreq += 1

        node.freq += 1
        dll = self.frequencies[node.freq]
        dll.append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._update(node)
            return

        if len(self.nodes) >= self.capacity:
            dll = self.frequencies[self.leastFreq]
            node = dll.pop()
            del self.nodes[node.key]
            del node

        node = Node(key, value)
        self.nodes[key] = node
        dll = self.frequencies[node.freq]
        self.leastFreq = 1
        dll.append(node)


def execute(cmds, inputs):
    res = []
    lfuCache = None

    for cmd, input in zip(cmds, inputs):
        # print(cmd, input)
        if cmd == 'LFUCache':
            capacity = input[0]
            lfuCache = LFUCache(capacity)
            ret = None
        elif cmd == 'put':
            key, value = input
            ret = lfuCache.put(key, value)
        elif cmd == 'get':
            key = input[0]
            ret = lfuCache.get(key)

        # print(lfuCache.freqMap)
        res.append(ret)

    print(res)


cmds = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
execute(cmds, inputs)

cmds = ["LFUCache","put","put","put","put","get"]
inputs = [[2],[3,1],[2,1],[2,2],[4,4],[2]]
execute(cmds, inputs)

cmds = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
inputs = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
execute(cmds, inputs)

cmds = ["LFUCache","put","get"]
inputs = [[0],[0,0],[0]]
execute(cmds, inputs)

cmds = ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
inputs = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
execute(cmds, inputs)

"""
Good explanation of solution:
https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
"""
