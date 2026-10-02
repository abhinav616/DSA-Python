s = "hello"
stack = []

for ch in s:
    stack.append(ch)

reverse = ""

while stack:
    reverse += stack.pop()

print(reverse)
