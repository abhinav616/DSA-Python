arr = [5, 7, 3, 4, 2]

stack = []
result = [-1] * len(arr)

for i in range(len(arr)):

    while stack and stack[-1] <= arr[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(arr[i])

print(result)
