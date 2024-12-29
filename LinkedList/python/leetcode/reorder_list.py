"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Very elegantly explanined solution in editorial with diagrams
    """
    Find a middle node of the linked list.
    If there are two middle nodes, return the second middle node.
    Example: for the list 1->2->3->4->5->6, the middle element is 4.
    
    Once a middle node has been found, reverse the second part of the list.
    Example: convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4.
    
    Now merge the two sorted lists.
    Example: merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4.
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = second
            second = temp
        

"""
Solution that uses memory:

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        linkedMap = {}
        count = 0
        maxCount = 0

        while head:
            linkedMap[count] = head
            maxCount = max(maxCount, count)
            count += 1
            head = head.next

        temp = prev = ListNode()
        i, j = 0, maxCount
        count = 0
        
        while count <= maxCount:
            if count % 2 == 0:
                node = linkedMap[i]
                i += 1
            else:
                node = linkedMap[j]
                j -= 1
            count += 1
            prev.next = node
            node.next = None # this is imp so it does not loop
            prev = node
"""

        return temp.next
        
