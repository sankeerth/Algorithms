"""
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:
Input: nums = [-1]
Output: [0]

Example 3:
Input: nums = [-1,-1]
Output: [0,0]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        nums = [(num, i) for i, num in enumerate(nums)]

        def countSmallerRecursive(l, r):
            if l+1 == r:
                return
            
            mid = (l + r) // 2
            countSmallerRecursive(l, mid)
            countSmallerRecursive(mid, r)

            i, j = l, mid
            while i < mid:
                while j < r and nums[j][0] < nums[i][0]:
                    j += 1
                res[nums[i][1]] += j - mid
                i += 1

            temp = [0] * (r-l)
            i, j, k = l, mid, 0
            while i < mid and j < r:
                if nums[i][0] <= nums[j][0]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            
            while i < mid:
                temp[k] = nums[i]
                i += 1
                k += 1
            
            while j < r:
                temp[k] = nums[j]
                j += 1
                k += 1
            
            nums[l:r] = temp
        
        countSmallerRecursive(0, len(nums))
        return res


sol = Solution()
print(sol.countSmaller([6]))
print(sol.countSmaller([4, 2]))
print(sol.countSmaller([2, 4]))
print(sol.countSmaller([4, 2, 3, 1]))
print(sol.countSmaller([2, 2, 4, 2]))
print(sol.countSmaller([4, 3, 2, 1]))
print(sol.countSmaller([2, 2, 2, 2]))
print(sol.countSmaller([1, 2, 3, 4]))


"""
My simpler solution:

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        nums = [(num, i) for i, num in enumerate(nums)]

        def countSmallerRecursive(l, r):
            if l+1 == r:
                return
            
            mid = (l + r) // 2
            countSmallerRecursive(l, mid)
            countSmallerRecursive(mid, r)

            i, j = l, mid
            while i < mid:
                while j < r and nums[j][0] < nums[i][0]:
                    j += 1
                res[nums[i][1]] += j - mid
                i += 1

            nums[l:r] = sorted(nums[l:r], key=lambda x: x[0]) # instead of custom merge
        
        countSmallerRecursive(0, len(nums))
        return res
"""
