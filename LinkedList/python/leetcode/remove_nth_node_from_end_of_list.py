"""
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(array):
    if not array:
        return None

    head = ListNode(array[0])
    temp = head
    for val in array[1:]:
        temp.next = ListNode(val)
        temp = temp.next

    return head


def print_linked_list(head):
    if not head:
        return None
    array = list()
    while head:
        array.append(head.val)
        head = head.next

    print(array)


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        fast = head
        slow = head
        prev_slow = None

        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            prev_slow = slow
            slow = slow.next

        if prev_slow:
            prev_slow.next = slow.next
            del slow
        else:
            temp = head
            head = head.next
            del temp

        return head

sol = Solution()
print_linked_list(sol.removeNthFromEnd(build_linked_list([1,2,3,4,5]), 3))
print_linked_list(sol.removeNthFromEnd(build_linked_list([1,2,3,4,5]), 1))
print_linked_list(sol.removeNthFromEnd(build_linked_list([1,2,3,4,5]), 5))
