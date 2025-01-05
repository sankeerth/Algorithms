"""
295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
import heapq


class MedianFinder(object):
    """
    Another really good solution with BST approach, although addNum and findNum both have O(log(N)) runtime.
    https://leetcode.com/problems/find-median-from-data-stream/discuss/74166/Solution-using-Binary-Search-Tree
    """
    """
    The idea is to use two heaps (one max heap, one mn heap) to save the input data. firstQ is a max_heap to save the
    first half of the data with smaller values, and secQ is a min_heap to save the second half of the data with bigger
    values. Everytime when inserting a new value, we first compare if it is smaller than the top of firstQ (the largest
    value of the first half), if so, insert into firstQ. Otherwise, it belongs to the second half. After inserting,
    we have to balance the first half and the second half to make sure either they have the same length or the length
    difference is only 1. The median will be the mean of two top elements (when they have the same length) or the
    top element of the queue with a larger length.
    """

    def __init__(self):
        self.lowerHalf = [] # max heap
        self.upperHalf = [] # min heap

    def addNum(self, num: int) -> None:
        if self.upperHalf and num > self.upperHalf[0]:
            heappush(self.upperHalf, num)
        else:
            heappush(self.lowerHalf, -num)

        if len(self.upperHalf) - len(self.lowerHalf) > 1:
            top = heappop(self.upperHalf)
            heappush(self.lowerHalf, -top)
        elif len(self.lowerHalf) - len(self.upperHalf) > 1:
            top = heappop(self.lowerHalf)
            heappush(self.upperHalf, -top)

    def findMedian(self) -> float:
        if len(self.lowerHalf) > len(self.upperHalf):
            return -self.lowerHalf[0]
        elif len(self.upperHalf) > len(self.lowerHalf):
            return self.upperHalf[0]
        else:
            return (-self.lowerHalf[0] + self.upperHalf[0]) / 2


med = MedianFinder()
med.addNum(6)
print(med.findMedian())
med.addNum(10)
print(med.findMedian())
med.addNum(2)
print(med.findMedian())
med.addNum(6)
print(med.findMedian())
med.addNum(5)
print(med.findMedian())
med.addNum(0)
print(med.findMedian())
med.addNum(6)
print(med.findMedian())
med.addNum(3)
print(med.findMedian())
med.addNum(1)
print(med.findMedian())
med.addNum(0)
print(med.findMedian())
med.addNum(0)
print(med.findMedian())

# print(med.findMedian())
# med.addNum(2)
# print(med.findMedian())
# med.addNum(5)
# print(med.findMedian())
# med.addNum(4)
# print(med.findMedian())
# med.addNum(1)
# print(med.findMedian())
# med.addNum(7)
# print(med.findMedian())


"""
leetcode discuss solution:
Supporting both min- and max-heap is more or less cumbersome, depending on the language, so I simply negate the numbers 
in the heap in which I want the reverse of the default order. To prevent this from causing a bug with -231 
(which negated is itself, when using 32-bit ints), I use integer types larger than 32 bits.

from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
"""
