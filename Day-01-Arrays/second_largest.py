arr = list(map(int, input().split()))

largest = arr[0]
second_largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest:
        second_largest = arr[i]

print("Second largest:", second_largest)
