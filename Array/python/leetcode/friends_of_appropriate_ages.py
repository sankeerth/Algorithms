"""
825. Friends Of Appropriate Ages

There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.

 

Example 1:

Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Constraints:

n == ages.length
1 <= n <= 2 * 104
1 <= ages[i] <= 120
"""
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        res = 0

        for ageOne, countOne in counter.items():
            for ageTwo, countTwo in counter.items():
                if ageOne < ageTwo:
                    continue
                if ageOne >= 2 * (ageTwo-7):
                    continue
                if ageOne < 100 and ageTwo > 100:
                    continue
                
                res += countOne * countTwo
                if ageOne == ageTwo:
                    res -= countOne
        
        return res


sol = Solution()
print(sol.numFriendRequests([16,16]))
print(sol.numFriendRequests([16,17,18,19]))
print(sol.numFriendRequests([20,30,100,110,120]))
print(sol.numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]))


"""
My solution that did not pass for last test case (need to figure out why this does not work):

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        ages.sort()
        i, j, k = 0, 0, 0

        while i < len(ages):
            while j < i and ages[i] >= 2 * (ages[j]-7):
                j += 1
            while k+1 < len(ages) and ages[k+1] == ages[i]:
                if ages[i] < 100 and ages[k+1] > 100:
                    break
                k += 1
            res += k-j
            i += 1

        return res
"""
