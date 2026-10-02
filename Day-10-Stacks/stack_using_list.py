stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

# Peek
print("Top:", stack[-1])

# Pop
print("Popped:", stack.pop())

# Stack after pop
print("Stack:", stack)

# Is Empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
