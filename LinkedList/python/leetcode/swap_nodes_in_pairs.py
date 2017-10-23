"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
from LinkedList.python.common.linked_list_operations import ListNode, build_linked_list, print_linked_list


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
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


sol = Solution()
print_linked_list(sol.swapPairs(build_linked_list([1,2,3,4,5])))
print_linked_list(sol.swapPairs(build_linked_list([1,2,3,4])))
print_linked_list(sol.swapPairs(build_linked_list([1,2,3,4,5,6])))
