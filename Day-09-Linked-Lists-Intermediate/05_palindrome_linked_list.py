class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1


# Find middle
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next


# Reverse second half
prev = None
current = slow

while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node


# Compare both halves
first = head
second = prev

is_palindrome = True

while second is not None:

    if first.data != second.data:
        is_palindrome = False
        break

    first = first.next
    second = second.next


if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
