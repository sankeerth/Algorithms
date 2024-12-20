"""
46. Permutations

Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutations(arr=list(), seen=set()):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            for num in nums:
                if num not in seen:
                    arr.append(num)
                    seen.add(num) # can add the index instead so it works for duplicate entries but has duplicate permuations in result
                    permutations(arr, seen)
                    arr.pop()
                    seen.discard(num)

        permutations()
        return res


sol = Solution()
sol.permute([1,2,3])
sol.permute([1])

"""
Solution using swap:

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def permute_recr(i, l):
            if i == l:
                copy = nums[:]
                result.append(copy)
                return
            for j in range(i, l):
                swap(i, j)
                permute_recr(i + 1, l)
                swap(i, j)

        permute_recr(0, len(nums))
        print(result)
"""
