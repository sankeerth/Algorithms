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


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapify(heap)

        head = ListNode(0)
        temp = head
        while heap:
            top = heappop(heap)
            node = top[2]
            if node.next:
                heappush(heap, (node.next.val, top[1], node.next))
            temp.next = node
            temp = temp.next

        return head.next


sol = Solution()
print_linked_list(sol.mergeKLists([build_linked_list([]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]))
print_linked_list(sol.mergeKLists([build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]))
print_linked_list(sol.mergeKLists([build_linked_list([4, 5, 6]), build_linked_list([2, 3]), build_linked_list([1, 7])]))
