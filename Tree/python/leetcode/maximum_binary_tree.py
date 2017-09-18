"""
654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
"""

from Tree.python.common.tree_operations import TreeNode, print_levelorder_leetcode_style


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)

        if length == 0:
            return None

        if length == 1:
            return TreeNode(nums[0])

        left = 0
        right = length - 1

        def constructMaximumBinaryTreeRecursive(left, right):
            if left > right:
                return None

            if left == right:
                return TreeNode(nums[left])

            max_index, max_val = max(enumerate(nums[left: right + 1]), key=lambda v: v[1])
            max_index += left
            root = TreeNode(max_val)
            root.left = constructMaximumBinaryTreeRecursive(left, max_index - 1)
            root.right = constructMaximumBinaryTreeRecursive(max_index + 1, right)

            return root

        return constructMaximumBinaryTreeRecursive(left, right)

sol = Solution()
print_levelorder_leetcode_style(sol.constructMaximumBinaryTree([3,2,1,6,0,5]))


"""
Disuss: C++ non recursive Solution using a simple stack

The key idea is:

We scan numbers from left to right, build the tree one node by one step;
We use a stack to keep some (not all) tree nodes and ensure a decreasing order;
For each number, we keep pop the stack until empty or a bigger number;
The bigger number (if exist, it will be still in stack) is current number's root,
and the last popped number (if exist) is current number's right child (temporarily, this relationship may change in the future);
Then we push current number into the stack.

class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> stk;
        for (int i = 0; i < nums.size(); ++i)
        {
            TreeNode* cur = new TreeNode(nums[i]);
            while (!stk.empty() && stk.back()->val < nums[i])
            {
                cur->left = stk.back();
                stk.pop_back();
            }
            if (!stk.empty())
                stk.back()->right = cur;
            stk.push_back(cur);
        }
        return stk.front();
    }
};
"""
