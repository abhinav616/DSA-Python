class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(5)
node2 = Node(6)
node3 = Node(100)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

current = head

while current.next is not None:
    if current.next.data == 100:
        current.next = current.next.next
        break
    current = current.next

current = head

while current is not None:
    print(current.data)
    current = current.next
