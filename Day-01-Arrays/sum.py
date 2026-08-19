arr = list(map(int, input().split()))

total = 0

for i in range(len(arr)):
    total = total + arr[i]

print(total)
