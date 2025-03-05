"""
362. Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to 
the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:
HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

Example 1:
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]
Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.

Constraints:
1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.

Follow up: What if the number of hits per second could be huge? Does your design scale?
"""


class HitCounter:
    def __init__(self):
        self.hits = []
        self.count = 0
        self.time = 300

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
            self.count += 1
            return

        self.hits.append([timestamp, 1])
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits:
            earliestTimestamp = self.hits[0][0]
            if timestamp - earliestTimestamp < self.time:
                break
            self.count -= self.hits[0][1]
            self.hits.pop(0)

        return self.count


def execute(cmds, inputs):
    hc = None
    res = []
    for cmd, input in zip(cmds, inputs):
        if cmd == 'HitCounter':
            hc = HitCounter()
            ret = None
        elif cmd == 'hit':
            ret = hc.hit(input[0])
        elif cmd == 'getHits':
            ret = hc.getHits(input[0])

        res.append(ret)

    return res


cmds = ["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]
inputs = [[],[1],[2],[3],[4],[300],[300],[301]]
print(execute(cmds, inputs))


"""
Uses more memory since only timestamp is appended:

class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxTimestamp = 300
        self.hits = list()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.hits and (timestamp - self.maxTimestamp) >= self.hits[0]:
            self.hits.pop(0)

        return len(self.hits)
"""
