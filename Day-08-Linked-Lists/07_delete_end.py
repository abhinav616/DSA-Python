class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(5)
node2 = Node(6)
node3 = Node(100)

node1.next = node2
node2.next = node3

head = node1

current = head

while current.next.next is not None:
    current = current.next

current.next = None

current = head

while current is not None:
    print(current.data)
    current = current.next
