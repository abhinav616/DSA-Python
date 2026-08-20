arr = list(map(int, input().split()))

k = int(input("Enter number of rotations: "))

n = len(arr)

for j in range(k):
    first = arr[0]

    for i in range(n - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first

print(arr)
