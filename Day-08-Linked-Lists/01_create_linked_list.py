class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(5)
node2 = Node(6)
node3 = Node(100)
node4 = Node(8)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1
