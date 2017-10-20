"""
34. Search for a Range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(low, high, target):
            while low <= high:
                mid = low + int((high - low) / 2)
                if nums[mid] == target:
                    return (mid, low, high)
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return None

        range = [float('inf'), float('-inf')]
        queue = list()
        queue.append((0, len(nums)-1))

        while queue:
            l, h = queue.pop(0)
            res = binary_search(l, h, target)
            if res:
                if res[0] < range[0]:
                    range[0] = res[0]
                    queue.append((res[1], res[0] - 1))

                if res[0] > range[1]:
                    range[1] = res[0]
                    queue.append((res[0] + 1, res[2]))

        if range[0] == float('inf'):
            return [-1, -1]
        else:
            return range

sol = Solution()
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 4))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 5))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 7))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 8))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 9))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 11))
