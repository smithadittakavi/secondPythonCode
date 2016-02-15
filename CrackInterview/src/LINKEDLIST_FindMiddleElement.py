# Find Middle Element in linked list 

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def create_linked_list(n):
    """Creating linked list for the given
       size"""
    linked_list = Node(1)
    head = linked_list
    for i in range(2, n):
        head.next = Node(i)
        head = head.next
    return linked_list

def print_linked_list(node):
    """To print the linked list in forward"""
    while node:
        print('[',node,']','[ref] ->')
        node = node.next
    print('-> None')

def find_middle(node):
    tick = False
    half = node
    while node:
        node = node.next
        if (tick):
            half = half.next
        tick = not tick
    return "Middle node is %s" % str(half)

node = create_linked_list(9)
print_linked_list(node)

print(find_middle(node))
#print(find_middle2(node))