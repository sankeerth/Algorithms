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