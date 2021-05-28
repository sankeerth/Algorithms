"""
1423. Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points.
The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row.
You have to take exactly k cards. Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:
Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 

Example 5:
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202

Constraints:
1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        
        i, j = 0, len(cardPoints)-k
        total = res = sum(cardPoints[j:])

        while i < k:
            total -= cardPoints[j]
            total += cardPoints[i]
            res = max(res, total)
            
            j += 1
            i += 1

        return res


s = Solution()
print(s.maxScore([1,2,3,4,5,6,1], 3))
print(s.maxScore([2,2,2], 2))
print(s.maxScore([2,2,2], 3))
print(s.maxScore([1,1000,1], 1))
print(s.maxScore([9,7,7,9,7,7,9], 3))
print(s.maxScore([9,7,7,9,7,7,9], 7))
print(s.maxScore([1,79,80,1,1,1,200,1], 3))


"""
Not an efficient solution since it takes O(n) space

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        result = 0
        maxFromLeft, maxFromRight = [0] * (len(cardPoints)+1), [0] * (len(cardPoints)+1)

        for i in range(len(cardPoints)):
            maxFromLeft[i+1] = maxFromLeft[i] + cardPoints[i]
        
        for i in range(len(cardPoints)-1, -1, -1):
            maxFromRight[i] = maxFromRight[i+1] + cardPoints[i]

        i, j = k, len(cardPoints)
        while i >= 0:
            result = max(result, maxFromLeft[i] + maxFromRight[j])
            i -= 1
            j -= 1
        
        return result
"""
