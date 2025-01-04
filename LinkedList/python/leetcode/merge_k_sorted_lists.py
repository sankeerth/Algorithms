"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
from LinkedList.python.common.linked_list_operations import ListNode, build_linked_list, print_linked_list
from heapq import heappush, heappop, heapify


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = ListNode()
        heap = []

        for i, node in enumerate(lists):
            # 2nd parameter in tuple is 'i' since 2nd parameter is used if 1st parameter (val) is same. If the 2nd parameter is of type ListNode,
            # then an error is thrown since '<' (cmp) is not defined on the class.
            if node:
                heappush(heap, (node.val, i, node))

        prev = head
        while heap:
            _, i, node = heappop(heap)
            prev.next = node
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
            prev = node

        return head.next


sol = Solution()
print_linked_list(sol.mergeKLists([build_linked_list([]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]))
print_linked_list(sol.mergeKLists([build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]))
print_linked_list(sol.mergeKLists([build_linked_list([4, 5, 6]), build_linked_list([2, 3]), build_linked_list([1, 7])]))
