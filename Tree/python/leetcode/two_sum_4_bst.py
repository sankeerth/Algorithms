"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
from Tree.python.common.tree_operations import deserialize


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        keys = dict()

        def preorder(root):
            if not root:
                return False
            else:
                if root.val in keys:
                    return True
                keys[k - root.val] = 1
                return preorder(root.left) or preorder(root.right)

        return preorder(root)

sol = Solution()
print(sol.findTarget(deserialize('[5,3,6,2,4,null,7]'), 9))
print(sol.findTarget(deserialize('[5,3,6,2,4,null,7]'), 11))
print(sol.findTarget(deserialize('[5,3,6,2,4,null,7]'), 28))


"""
One of the leetcode solutions

In this approach, we make use of the fact that the given tree is a Binary Search Tree. Now, we know that the inorder traversal of a BST gives the nodes in ascending order.
Thus, we do the inorder traversal of the given tree and put the results in a listlist which contains the nodes sorted in ascending order.
Once this is done, we make use of two pointers ll and rr pointing to the beginning and the end of the sorted listlist. Then, we do as follows:
Check if the sum of the elements pointed by ll and rr is equal to the required sum kk. If so, return a True immediately.
Otherwise, if the sum of the current two elements is lesser than the required sum kk, update ll to point to the next element.
This is done, because, we need to increase the sum of the current elements, which can only be done by increasing the smaller number.
Otherwise, if the sum of the current two elements is larger than the required sum kk, update rr to point to the previous element.
This is done, because, we need to decrease the sum of the current elements, which can only be done by reducing the larger number.
Continue steps 1. to 3. till the left pointer ll crosses the right pointer rr.
If the two pointers cross each other, return a False value.

public class Solution {
    public boolean findTarget(TreeNode root, int k) {
        List < Integer > list = new ArrayList();
        inorder(root, list);
        int l = 0, r = list.size() - 1;
        while (l < r) {
            int sum = list.get(l) + list.get(r);
            if (sum == k)
                return true;
            if (sum < k)
                l++;
            else
                r--;
        }
        return false;
    }
    public void inorder(TreeNode root, List < Integer > list) {
        if (root == null)
            return;
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }
}
"""
