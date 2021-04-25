"""
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
from LinkedList.python.common.linked_list_operations import ListNode, build_linked_list, print_linked_list


class Solution(object):
    def removeNthFromEnd(self, head, n):
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


"""
Leetcode solution: A little simpler solution using Dummy node as the first node.

The first pointer advances the list by n+1n+1 steps from the beginning, while the second pointer starts 
from the beginning of the list. Now, both pointers are exactly separated by nn nodes apart. 
We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. 
The second pointer will be pointing at the nnth node counting from the last. 
We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy

        for _ in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next
"""
