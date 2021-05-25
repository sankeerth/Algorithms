"""
364. Nested List Weight Sum II

The depth of an integer is the number of lists that it is inside of. 
For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. 
Let maxDepth be the maximum depth of any integer.
The weight of an integer is maxDepth - (the depth of the integer) + 1.
Return the sum of each integer in nestedList multiplied by its weight.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17

Constraints:
1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.
"""
from typing import List


#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from typing import List
from collections import defaultdict


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        sumAtDepth = defaultdict(int)
        res = 0

        def depthRecursive(nestedList, curDepth):
            depth = 0
            for item in nestedList:
                if item.isInteger():
                    sumAtDepth[curDepth] += item.getInteger()
                else:
                    depth = max(depth, depthRecursive(item.getList(), curDepth+1))
            
            return max(curDepth, depth)

        maxDepth = depthRecursive(nestedList, 1)
        for depth, depthSum in sumAtDepth.items():
            res += depthSum * (maxDepth-depth+1)

        return res


sol = Solution()
print(sol.depthSumInverse([[1,1],2,[1,1]]))
print(sol.depthSumInverse([1,[4,[6]]]))
print(sol.depthSumInverse([[],[],[]]))


"""
BFS solution from leetcode:

class Solution(object):
    def depthSumInverse(self, nestedList):
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum
"""        

"""
Solution by traversing each integer instead of sum per depth stored in dict:

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        numsWithDepths, res = [], 0
        
        def depthSumInverseRecursive(nestedList, depth):
            maxDepth = depth
            for item in nestedList:
                if item.isInteger():
                    numsWithDepths.append((item.getInteger(), depth))
                else:
                    curDepth = depthSumInverseRecursive(item.getList(), depth+1)
                    maxDepth = max(maxDepth, curDepth)
            
            return maxDepth

        maxDepth = depthSumInverseRecursive(nestedList, 1)

        for num, depth in numsWithDepths:
            res += num * (maxDepth-depth+1)

        return res
"""
