"""
493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3

Discuss URL explanation: https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22
Imp: see the other approaches and detailed explanation in it
"""


class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if not nums:
            return result

        def merge_sort(lo, hi):
            nonlocal result
            if lo >= hi:
                return
            mid = int(lo + (hi - lo)/2)
            merge_sort(lo, mid)
            merge_sort(mid+1, hi)

            temp = [0] * (hi-lo+1)
            i, j = lo, mid+1

            while i <= mid:
                while j <= hi and nums[i] > 2 * nums[j]:
                    j += 1
                result += j - (mid+1)
                i += 1

            i, j, k = lo, mid + 1, 0
            while i <= mid and j <= hi:
                if nums[i] < nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j <= hi:
                temp[k] = nums[j]
                j += 1
                k += 1

            nums[lo:hi+1] = temp[:]

        merge_sort(0, len(nums)-1)
        return result


sol = Solution()
print(sol.reversePairs([3, 1]))
print(sol.reversePairs([6, 5, 2, 1]))
print(sol.reversePairs([1, 2, 5, 6]))
print(sol.reversePairs([1, 3, 2, 3, 1]))
print(sol.reversePairs([2, 4, 3, 5, 1]))
print(sol.reversePairs([4, 1, 1, 2]))
print(sol.reversePairs([-8, -5, -4]))
print(sol.reversePairs([-5, -5]))
print(sol.reversePairs([-4, -6, 2, -3]))
print(sol.reversePairs([-8, -5, -4, -7]))
print(sol.reversePairs([-1, -2, -3, -4]))
print(sol.reversePairs([-4, -3, -2, -1]))

"""
leetcode discuss solution:

class Solution:
     def reversePairs(self, nums):
        def mergesort(lo, hi):
            m = (lo + hi) // 2
            if m == lo: return 0
            count = mergesort(lo, m) + mergesort(m, hi)
            j = m
            for i in range(lo, m):
                while j < hi and nums[i] > 2 * nums[j]: j += 1
                count += j - m
            nums[lo:hi] = sorted(nums[lo:hi])
            return count
        return mergesort(0, len(nums))
"""