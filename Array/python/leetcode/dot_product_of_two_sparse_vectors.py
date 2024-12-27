"""
1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:
SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
Follow up: What if only one of the vectors is sparse?

Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.values[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        # take the smaller map as outer loop to reduce complexity => O(min(N1, N2)) where N1 and N2 are number of non-zero values of vectors v1 and v2
        if len(self.values) < len(vec.values):
            map1, map2 = self.values, vec.values
        else:
            map1, map2 = vec.values, self.values

        for i in map1:
            if i in map2:
                res += map1[i] * map2[i]

        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
