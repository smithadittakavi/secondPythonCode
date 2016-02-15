class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
    


def deleteNode(node):
    if node and node.next:
        node_to_delete = node.next
        node.val = node_to_delete.val
        node.next = node_to_delete.next
        del node_to_delete
    
       
def print_list(node):
    while node:
        print(node)
        node = node.next
    print(node)
    

              
def delete_by_index(node, index):
    if not index:
        return node.next
    head = node
    for _ in range(index):
        prev_node, node = node, node.next
    prev_node.next = node.next
    return head
            
def findMiddle(node):
    temp = False
    half = node
    while node:
        node = node.next
        if(temp):
            half = half.next
        temp = not temp
    return "Middle Node is : %s"% str(half)

# way of creating linked list
def create_linked_list1(n):
    linked_list = Node(1)
    head = linked_list
    for i in range(2, n):
        head.next = Node(i)
        head = head.next
    return linked_list

node1 = create_linked_list1(4)


        
        
print_list(node1)
print('\n')

deleteNode(2)
print_list(node1)
#delete_by_index(node1, 1)
#print_list(node1)
#print(findMiddle(node1))


