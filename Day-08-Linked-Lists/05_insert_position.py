class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(5)
node2 = Node(6)
node3 = Node(8)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

new_node = Node(100)

current = node2

new_node.next = current.next
current.next = new_node

current = head

while current is not None:
    print(current.data)
    current = current.next
