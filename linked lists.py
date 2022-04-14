class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev
        
def print_linked_list(vertex):
        while vertex:
                print(vertex.value, end=" -> ")
                vertex = vertex.next
        print("None") 

def get_node_by_index(node, index):
        while index:
                node = node.next
                index -= 1
        return node

def insert_node(head, index, value):
        new_node = Node(value)
        if index == 0:
                new_node.next = head
                return new_node
        previous_node = get_node_by_index(head, index-1)
        new_node.next = previous_node.next 
        previous_node.next = new_node
        return head

def delete_node(head, index):
        if index == 0:
                head = head.next
                return head
        previous_node = get_node_by_index(head, index-1)
        del_node = previous_node.next
        previous_node.next = del_node.next
        return head

def found_index(node, elem):
    idx = 0
    while node:
        if node.value == elem:
            return idx
        node = node.next
        idx += 1
    return -1

def reverse_list(node):
    while node.next:
        node.next, node.prev = node.prev, node.next
        node = node.prev
    node.next, node.prev = node.prev, node.next
    return node

# n3 = Node('third')
# n2 = Node('second', n3)
# n1 = Node('first', n2)
# n0 = Node('zero', n1)

# node, index, value = n0, 1, 'new_node'
# head = insert_node(node, index, value) 

# head, index = n0, 2
# head = delete_node(head, index)

# print_linked_list(head)

# print(found_index(n0, 'second'))

n3 = DoubleConnectedNode('third')
n2 = DoubleConnectedNode('second')
n1 = DoubleConnectedNode('first')
n0 = DoubleConnectedNode('zero')

n0.next = n1

n1.next = n2
n1.prev = n0

n2.next = n3
n2.prev = n1

n3.prev = n2


head = n0
rev_head = reverse_list(head)
print_linked_list(rev_head)