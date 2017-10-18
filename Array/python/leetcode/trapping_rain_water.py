"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        l = len(height)
        max_height_to_left = [0] * l
        max_height_to_right = [0] * l

        max_height_to_left[0] = height[0]
        max_height_to_right[l - 1] = height[l - 1]

        for i in range(1, l):
            max_height_to_left[i] = max(max_height_to_left[i - 1], height[i])
            max_height_to_right[l - i - 1] = max(max_height_to_right[l - i], height[l - i - 1])

        rain_water_trapped = 0
        for i in range(l):
            rain_water_trapped += min(max_height_to_left[i], max_height_to_right[i]) - height[i]

        return rain_water_trapped

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([2,4,3,6,9,5]))

"""
Leetcode discuss solution: O(n) time, O(1) space

instead of calculating area by height*width, we can think it in a cumulative way.
In other words, sum water amount of each bin(width=1).
Search from left to right and maintain a max height of left and right separately, which is like a one-side wall of partial container.
Fix the higher one and flow water from the lower part.
For example, if current height of left is lower, we fill water in the left bin. Until left meets right, we filled the whole container.

class Solution {
public:
    int trap(int A[], int n) {
        int left=0; int right=n-1;
        int res=0;
        int maxleft=0, maxright=0;
        while(left<=right){
            if(A[left]<=A[right]){
                if(A[left]>=maxleft) maxleft=A[left];
                else res+=maxleft-A[left];
                left++;
            }
            else{
                if(A[right]>=maxright) maxright= A[right];
                else res+=maxright-A[right];
                right--;
            }
        }
        return res;
    }
};
"""