class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(3)
node6 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

current = head

while current is not None and current.next is not None:

    if current.data == current.next.data:
        current.next = current.next.next
    else:
        current = current.next


current = head

while current is not None:
    print(current.data)
    current = current.next
