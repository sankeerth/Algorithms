"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

Follow up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1, maj2, count1, count2 = float('inf'), float('inf'), 0, 0
        res = []

        for num in nums:
            if num == maj1:
                count1 += 1
            elif num == maj2:
                count2 += 1
            elif count1 == 0:
                maj1 = num
                count1 += 1
            elif count2 == 0:
                maj2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == maj1:
                count1 += 1
            elif num == maj2:
                count2 += 1
        
        if count1 > len(nums)//3:
            res.append(maj1)
        if count2 > len(nums)//3:
            res.append(maj2)

        return res


sol = Solution()
print(sol.majorityElement([1]))
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,2,3,4,5,2,2,5]))
print(sol.majorityElement([2,4,2,5,3]))
print(sol.majorityElement([2,4,2,5,2,3]))
print(sol.majorityElement([2,4,2,5,3,2]))
print(sol.majorityElement([5,2,4,2,1,2,2,3,2,1]))


"""
Intuition

To figure out a O(1) space requirement, we would need to get this simple intuition first. For an array of length n:

There can be at most one majority element which is more than ⌊n/2⌋ times.
There can be at most two majority elements which are more than ⌊n/3⌋ times.
There can be at most three majority elements which are more than ⌊n/4⌋ times.
and so on.

Knowing this can help us understand how we can keep track of majority elements which satisfies O(1) space requirement.

--- Majority Element > N/2 ---

Let's try to get an intuition for the case where we would like to find a majority element which is more than ⌊n/2⌋ times in an array of length n.
The idea is to have two variables, one holding a potential candidate for majority element and a counter to keep track of whether to swap a potential candidate or not. 
Why can we get away with only two variables? Because there can be at most one majority element which is more than ⌊n/2⌋ times. 
Therefore, having only one variable to hold the only potential candidate and one counter is enough.

While scanning the array, the counter is incremented if you encounter an element which is exactly same as the potential candidate but decremented otherwise. 
When the counter reaches zero, the element which will be encountered next will become the potential candidate. Keep doing this procedure while scanning the array. 
However, when you have exhausted the array, you have to make sure that the element recorded in the potential candidate variable is the majority element by checking whether it occurs 
more than ⌊n/2⌋ times in the array. In the original Majority Element problem, it is guaranteed that there is a majority element in the array so your implementation can omit the second pass. 
However, in a general case, you need this second pass since your array can have no majority elements at all!

The counter is initialized as 0 and the potential candidate as None at the start of the array.
If an element is truly a majority element, it will stick in the potential candidate variable, no matter how it shows up in the array (i.e. all clustered in the beginning of the array, 
all clustered near the end of the array, or showing up anywhere in the array), after the whole array has been scanned. Of course, while you are scanning the array, 
the element might be replaced by another element in the process, but the true majority element will definitely remain as the potential candidate in the end.

--- Majority Element > N/3 ---

Now figuring out the majority elements which show up more than ⌊n/3⌋ times is not that hard anymore. Using the intuition presented in the beginning, we only need four variables: 
two for holding two potential candidates and two for holding two corresponding counters. 
Similar to the above case, both candidates are initialized as None in the beginning with their corresponding counters being 0. While going through the array:

If the current element is equal to one of the potential candidate, the count for that candidate is increased while leaving the count of the other candidate as it is.
If the counter reaches zero, the candidate associated with that counter will be replaced with the next element if the next element is not equal to the other candidate as well.
Both counters are decremented only when the current element is different from both candidates.
"""
