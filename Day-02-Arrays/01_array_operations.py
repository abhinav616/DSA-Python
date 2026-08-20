arr = list(map(int, input().split()))

# Traversal
for i in range(len(arr)):
    print(arr[i])

# Updating
arr[0] = 100

# Insertion
arr.insert(1, 50)

# Deletion by index
arr.pop(2)

# Searching
target = 50

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
