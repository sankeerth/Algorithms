"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
"""


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __repr__(self):
        return 'Node({})|Random({})'.format(self.label, self.random)


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

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        nodes = dict()
        start = RandomListNode(head.label)
        nodes[head] = start
        list1 = head.next
        list2 = start

        while list1:
            list2.next = RandomListNode(list1.label)
            list2 = list2.next
            nodes[list1] = list2
            list1 = list1.next

        list1 = head
        while list1:
            if list1.random:
                random_node = list1.random
                copy_node = nodes[list1]
                copy_node.random = nodes[random_node]
            list1 = list1.next

        return start


def build_linked_list(array):
    if not array:
        return None

    head = RandomListNode(array[0])
    temp = head
    for val in array[1:]:
        temp.next = RandomListNode(val)
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
        array.append(head.label)
        head = head.next

    print(array)


sol = Solution()
print_linked_list(sol.copyRandomList(build_linked_list([1, 2, 3, 4, 5])))
