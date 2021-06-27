"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""
from LinkedList.python.common.linked_list_operations import ListNode, print_linked_list, build_linked_list


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if not l1 and not l2:
            return None

        head = ListNode(0)
        node = head
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = carry + x + y
            carry = total // 10

            node.next = ListNode(total % 10)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            node.next = ListNode(carry)

        return head.next


sol = Solution()
print_linked_list(sol.addTwoNumbers(build_linked_list([2, 4]), build_linked_list([5, 2, 3])))
print_linked_list(sol.addTwoNumbers(build_linked_list([2, 8]), build_linked_list([5, 2, 3])))
print_linked_list(sol.addTwoNumbers(build_linked_list([2]), build_linked_list([9])))
