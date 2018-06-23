"""
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

from LinkedList.python.common.linked_list_operations import ListNode, build_linked_list, print_linked_list


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node

        return new_head


sol = Solution()
print_linked_list(sol.reverseList(build_linked_list([1, 2, 3, 4, 5])))
print_linked_list(sol.reverseList(build_linked_list([1, 2])))
print_linked_list(sol.reverseList(build_linked_list([1])))
print_linked_list(sol.reverseList(build_linked_list([])))

