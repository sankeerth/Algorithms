"""
981. Time Based Key-Value Store

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)
Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)
Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").

Example 1:
Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:
Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]

Note:
All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""


class TimeMap:
    def __init__(self):
        self.keyValueStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValueStore:
            self.keyValueStore[key] = []
        self.keyValueStore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        def binarySearch(key, timestamp, lo, hi):
            tuples = self.keyValueStore[key]
            while lo <= hi:
                mid = (lo + hi) // 2
                if lo == hi:
                    return tuples[lo]
                elif tuples[mid][1] <= timestamp < tuples[mid+1][1]:
                    return tuples[mid]
                else:
                    if timestamp < tuples[mid][1]:
                        hi = mid - 1
                    else:
                        lo = mid + 1

        if key not in self.keyValueStore or self.keyValueStore[key][0][1] > timestamp:
            return ""

        lo, hi = 0, len(self.keyValueStore[key])-1
        value, timestamp = binarySearch(key, timestamp, lo, hi)
        return value


def execute(cmds, inputs):
    timemap = None
    res = []

    for cmd, input in zip(cmds, inputs):
        if cmd == 'TimeMap':
            timemap = TimeMap()
            ret = None
        elif cmd == 'set':
            key, value, timestamp = input
            ret = timemap.set(key, value, timestamp)
        elif cmd == 'get':
            key, timestamp = input
            ret = timemap.get(key, timestamp)
        res.append(ret)
    return res


cmds = ["TimeMap","set","get","get","set","get","get"]
inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
print(execute(cmds, inputs))

cmds = ["TimeMap","set","get","get","set","get","get"]
inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",3]]
print(execute(cmds, inputs))

cmds = ["TimeMap","set","get","get","set","get","get"]
inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",0]]
print(execute(cmds, inputs))
