"""
315. Count of Smaller Numbers After Self


You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        indices = [i for i in range(len(nums))]
        if not nums:
            return result

        def merge_sort(lo, hi):
            if lo >= hi:
                return
            mid = int(lo + (hi - lo)/2)
            merge_sort(lo, mid)
            merge_sort(mid+1, hi)
            merge(lo, hi, mid)

        def merge(lo, hi, mid):
            i, j, k, count = lo, mid+1, 0, 0
            temp = [0] * (hi-lo+1)
            index = [0] * (hi-lo+1)

            while i <= mid and j <= hi:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    result[indices[i]] += count
                    index[k] = indices[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    count += 1
                    index[k] = indices[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = nums[i]
                result[indices[i]] += count
                index[k] = indices[i]
                i += 1
                k += 1

            while j <= hi:
                temp[k] = nums[j]
                index[k] = indices[j]
                j += 1
                k += 1

            nums[lo:hi+1] = temp[:]
            indices[lo:hi+1] = index[:]

        merge_sort(0, len(nums)-1)
        return result


sol = Solution()
print(sol.countSmaller([6]))
print(sol.countSmaller([4, 2]))
print(sol.countSmaller([2, 4]))
print(sol.countSmaller([4, 2, 3, 1]))
print(sol.countSmaller([2, 2, 4, 2]))
print(sol.countSmaller([4, 3, 2, 1]))
print(sol.countSmaller([2, 2, 2, 2]))
print(sol.countSmaller([1, 2, 3, 4]))


'''
My simpler solution:

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        nums = list(enumerate(nums))

        def count_smaller_recr(lo, hi):
            if lo >= hi:
                return

            mid = (lo + hi) // 2
            count_smaller_recr(lo, mid)
            count_smaller_recr(mid+1, hi)

            i, j = lo, mid+1
            while i <= mid:
                while j <= hi and nums[i][1] > nums[j][1]:
                    j += 1
                result[nums[i][0]] += j - mid - 1
                i += 1
            nums[lo: hi+1] = sorted(nums[lo:hi+1], key=lambda x: x[1])

        count_smaller_recr(0, len(nums)-1)

        return result
'''
