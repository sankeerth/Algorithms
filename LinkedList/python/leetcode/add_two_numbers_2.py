"""
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?
"""
from LinkedList.python.common.linked_list_operations import ListNode, print_linked_list, build_linked_list


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        stack1 = list()
        stack2 = list()

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        res = None
        carry = 0
        while stack1 or stack2:
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            total = (a + b + carry) % 10  # need to add carry here, corner case: a=5, b=4, carry=1
            node = ListNode(total)
            node.next = res
            res = node
            carry = (a + b + carry) // 10  # if carry not added here then it fails for last 2 test cases

        if carry:
            node = ListNode(carry)
            node.next = res
            res = node

        return res


sol = Solution()
print_linked_list(sol.addTwoNumbers(build_linked_list([7, 2, 4, 3]), build_linked_list([5, 6, 4])))
print_linked_list(sol.addTwoNumbers(build_linked_list([7, 2, 4, 4]), build_linked_list([6])))
print_linked_list(sol.addTwoNumbers(build_linked_list([7, 2, 4, 3]), build_linked_list([5, 7])))
print_linked_list(sol.addTwoNumbers(build_linked_list([7, 2, 4, 3]), build_linked_list([7, 5, 7])))
print_linked_list(sol.addTwoNumbers(build_linked_list([9, 2, 4, 3]), build_linked_list([7, 5, 7])))
