"""
406. Queue Reconstruction by Height

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). 
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people 
in front who have a height greater than or equal to hi.
Reconstruct and return the queue that is represented by the input array people. 
The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is 
the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:
1 <= people.length <= 2000
0 <= hi <= 106
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
"""


"""
Let's start from the simplest case, when all guys (h, k) in the queue are of the same height h, 
and differ by their k values only (the number of people in front who have a greater or the same height). 
Then the solution is simple: each guy's index is equal to his k value. The guy with zero people 
in front takes the place number 0, the guy with 1 person in front takes the place number 1, and so on and so forth.

This strategy could be used even in the case when not all people are of the same height. The smaller persons are 
"invisible" for the taller ones, and hence one could first arrange the tallest guys as if there was no one else.

Let's now consider a queue with people of two different heights: 7 and 6. For simplicity, let's have 
just one 6-height guy. First follow the strategy above and arrange guys of height 7. Now it's time 
to find a place for the guy of height 6. Since he is "invisible" for the 7-height guys, he could take
whatever place without disturbing 7-height guys order. However, for him the others are visible, and 
hence he should take the position equal to his k-value, in order to have his proper place.

The following strategy could be continued recursively:
- Sort the tallest guys in the ascending order by k-values and then insert them one by one into output 
queue at the indexes equal to their k-values.
- Take the next height in the descending order. Sort the guys of that height in the ascending order 
by k-values and then insert them one by one into output queue at the indexes equal to their k-values.
- And so on and so forth.

Algorithm

- Sort people:
  - In the descending order by height.
  - Among the guys of the same height, in the ascending order by k-values.
- Take guys one by one, and place them in the output array at the indexes equal to their k-values.
- Return output array.
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for person in people:
            result.insert(person[1], person)
        
        return result


s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))


"""
Leetcode discuss solution: 2 for loops without using 'Insert'

The number k means that we can put this person in the kth empty slot. 
When iterating through pos list where we reconstruct the people, 
if we see an empty slot or the slot is already placed with someone who has 
the same height, we can deduct the k by 1. When k becomes 0 and the slot is empty, 
that's the position where we want to place the person.

First, we need to sort the input by h and k in ASC order

input:  [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sorted: [[4,4], [5,0], [5,2], [6,1], [7,0], [7,1]]

Also, intialize the pos list with empty slots

 pos  =  [[   ], [   ], [   ], [   ], [   ], [   ]]

Place people to pos

[4,4] => [[   ], [   ], [   ], [   ], [4,4], [   ]]
[5,0] => [[5,0], [   ], [   ], [   ], [4,4], [   ]]
[5,2] => [[5,0], [   ], [5,2], [   ], [4,4], [   ]]
[6,1] => [[5,0], [   ], [5,2], [6,1], [4,4], [   ]]
[7,0] => [[5,0], [7,0], [5,2], [6,1], [4,4], [   ]]
[7,1] => [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(len(people))]
        people.sort(key=lambda x: (x[0], x[1]))
        
        for person in people:
            height, count = person
            for i in range(len(people)):
                if count == 0 and not res[i]:
                    # correct position of the person
                    res[i] = person
                    break
                
                if not res[i] or height == res[i][0]:
                    # this position is either occupied by taller person (> h) 
                    # or person with same height but smaller count (< k)
                    count -= 1
        
        return res
"""


"""
Heap with custom class

class People:
    __slots__ = ("h", "k")
    
    def __init__(self, h: int, k: int):  
        self.h: int = h
        self.k: int = k

    def __lt__(self, other: "People"):
        if self.h == other.h:
            return self.k <= other.k
        
        return self.h > other.h

    def __iter__(self):
        return iter((self.h, self.k))

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pq: List["People"] = []
        [heapq.heappush(pq, People(h, k)) for h, k in people]
            
        answers: List[List[int]] = []
        while pq:
            h, k = heapq.heappop(pq)
            answers.insert(k, [h, k])
        return answers
"""

"""
Simple heap solution

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap, res = [], []
        for h, k in people:
            heappush(heap, (-h, k))

        while heap:
            h, k = heappop(heap)
            res.insert(k, [-h, k])

        return res
"""
