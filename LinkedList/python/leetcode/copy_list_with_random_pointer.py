"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied 
list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:
Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.

Constraints:
0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random is null or is pointing to some node in the linked list.
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return 'Node({})|Random({})'.format(self.val, self.random)


class Solution(object):
    """
    Explanation:
        An intuitive solution is to keep a hash table for each node in the list, via which we just need to iterate the
        list in 2 rounds respectively to create nodes and assign the values for their random pointers. As a result,
        the space complexity of this solution is O(N), although with a linear time complexity.

        As an optimised solution, we could reduce the space complexity into constant. The idea is to associate the
        original node with its copy node in a single linked list. In this way, we don't need extra space to keep track of the new nodes.
        The algorithm is composed of the follow three steps which are also 3 iteration rounds.

        1. Iterate the original list and duplicate each node. The duplicate of each node follows its original immediately.
        2. Iterate the new list and assign the random pointer for each duplicated node.
        3. Restore the original list and extract the duplicated nodes.
    """
    def copyRandomList(self, head: Node) -> Node:
        nodesMap = {None: None}
        l1, res = head, Node(0)
        l2 = res

        while l1:
            node = Node(l1.val)
            l2.next = node
            l2 = node
            nodesMap[l1] = l2
            l1 = l1.next

        l1 = head
        while l1:
            copy, random = nodesMap[l1], nodesMap[l1.random]
            copy.random = random
            l1 = l1.next

        return res.next


def build_linked_list(array):
    if not array:
        return None

    head = Node(array[0])
    temp = head
    for val in array[1:]:
        temp.next = Node(val)
        temp = temp.next

    # assigning random pointers
    head.random = head.next.next
    head.next.random = head.next.next
    head.next.next.next.random = head

    return head


def print_linked_list(head):
    if not head:
        return None
    array = list()
    while head:
        array.append(head.val)
        head = head.next

    print(array)


sol = Solution()
print_linked_list(sol.copyRandomList(build_linked_list([1, 2, 3, 4, 5])))


"""
Leetcode solution with O(N) space (variant of mine)
In this, orginal list is traversed from head with next and random nodes pertaining to the new list 
created on the fly where corresponding node from original list is mapped to the node in new list. 
This is a similar idea but this is a one-pass solution.

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        nodesMap = {None: None}
        
        def getClonedNode(node):
            if node not in nodesMap:
                clone = Node(node.val)
                nodesMap[node] = clone

            return nodesMap[node]

        if not head:
            return head

        l1, l2 = head, Node(head.val)
        nodesMap[l1] = l2

        while l1:
            l2.next = getClonedNode(l1.next)
            l2.random = getClonedNode(l1.random)
            
            l1, l2 = l1.next, l2.next

        return nodesMap[head]
"""

"""
Approach 3: Iterative with O(1)O(1) Space
Intuition

Instead of a separate dictionary to keep the old node --> new node mapping, 
we can tweak the original linked list and keep every cloned node next to its original node. 
This interleaving of old and new nodes allows us to solve this problem without any extra space. 

Algorithm
Traverse the original list and clone the nodes as you go and place the cloned copy next 
to its original node. This new linked list is essentially a interweaving of original and cloned nodes.

As you can see we just use the value of original node to create the cloned copy. 
The next pointer is used to create the weaving. Note that this operation ends up modifying the original linked list.

 cloned_node.next = original_node.next
 original_node.next = cloned_node
 
Iterate the list having both the new and old nodes intertwined with each other and use the original nodes' 
random pointers to assign references to random pointers for cloned nodes. 
For eg. If B has a random pointer to A, this means B' has a random pointer to A'.

Now that the random pointers are assigned to the correct node, the next pointers need to 
be correctly assigned to unweave the current linked list and get back the original list and the cloned list.


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
"""
