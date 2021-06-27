"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]

Constraints:
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
"""
from LinkedList.python.common.linked_list_operations import ListNode, build_linked_list, print_linked_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        temp, start = head, head
        while temp:
            length += 1
            temp = temp.next

        def reverseLL(head):
            if not head:
                return None, None
            i = 0
            prev = None
            while i < k:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
                i += 1
            
            return prev, head

        times = int(length / k)
        reversed = ListNode(0)
        tail = reversed

        while times > 0:
            newHead, nextHead = reverseLL(start)
            tail.next = newHead
            tail = start
            start = nextHead

            times -= 1

        tail.next = nextHead
        return reversed.next


sol = Solution()
print_linked_list(sol.reverseKGroup(build_linked_list([1,2,3,4,5]), 2))
print_linked_list(sol.reverseKGroup(build_linked_list([1,2,3,4,5,6]), 2))
print_linked_list(sol.reverseKGroup(build_linked_list([1,2,3,4,5,6]), 3))
print_linked_list(sol.reverseKGroup(build_linked_list([1,2,3,4,5,6]), 4))
print_linked_list(sol.reverseKGroup(build_linked_list([1,2,3,4,5]), 3))


"""
Using extra stack space O(k) but modifying the same list:

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        stack = []
        temp, orignal = head, head
        while temp:
            length += 1
            temp = temp.next
        
        times = int(length / k)
        reversed, prev = None, None

        while times > 0:
            i = 0
            while i < k:
                stack.append(orignal)
                orignal = orignal.next
                i += 1
            
            while stack:
                top = stack.pop()
                if not reversed:
                    reversed = top
                if prev:
                    prev.next = top
                prev = top

            times -= 1
        
        prev.next = orignal
        return reversed
"""

"""
Using extra array space O(N) and creating a new LL:

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        array = []
        temp = head
        while temp:
            length += 1
            array.append(temp.val)
            temp = temp.next
        
        times = int(length / k)
        start, end = -1, k-1
        reversed = ListNode(0)
        tail = reversed
        
        while times > 0:
            for i in range(end, start, -1):
                node = ListNode(array[i])
                tail.next = node
                tail = node            
            
            start = end
            end += k
            times -= 1
        
        for i in range(start+1, length):
            node = ListNode(array[i])
            tail.next = node
            tail = node

        return reversed.next
"""
