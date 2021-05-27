"""
670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
0 <= num <= 108
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = list(str(num))
        point = 0

        def swap(i, j):
            numList[i], numList[j] = numList[j], numList[i]

        # find the point where the first increment happens
        for i in range(1, len(numList)):
            if numList[i] > numList[i-1]:
                point = i
                break

        # index of max value after increment is the new point
        for i in range(point+1, len(numList)):
            if numList[i] >= numList[point]:
                point = i

        # swap the point with the first value less than point starting from left
        for i in range(point):
            if numList[i] < numList[point]:
                swap(i, point)
                break
        
        return int("".join(numList))


sol = Solution()
print(sol.maximumSwap(2736))
print(sol.maximumSwap(9973))
print(sol.maximumSwap(4321))
print(sol.maximumSwap(123456))
print(sol.maximumSwap(91))
print(sol.maximumSwap(18))
print(sol.maximumSwap(183))
print(sol.maximumSwap(7))
print(sol.maximumSwap(0))
# Imp test cases
print(sol.maximumSwap(9187))
print(sol.maximumSwap(927883))
