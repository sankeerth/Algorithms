"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
from LinkedList.python.common.linked_list_operations import ListNode, build_linked_list, print_linked_list


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        one, prev = head, None
        head = one.next

        while one:
            two = one.next
            if not two:
                break
            one.next = two.next
            two.next = one
            if prev:
                prev.next = two
            prev = one
            one = one.next

        return head


sol = Solution()
print_linked_list(sol.swapPairs(build_linked_list([1,2,3,4,5])))
print_linked_list(sol.swapPairs(build_linked_list([1,2,3,4])))
print_linked_list(sol.swapPairs(build_linked_list([1,2,3,4,5,6])))


"""
class Solution(object):
    def swapPairs(self, head):
        new_node = head
        prev_node = None

        while new_node:
            temp = new_node.next
            if not temp:
                break
            new_node.next = temp.next
            temp.next = new_node
            if not prev_node:
                head = temp
            else:
                prev_node.next.next = temp
            prev_node = temp
            new_node = new_node.next

        return head
"""
