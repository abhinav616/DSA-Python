arr = list(map(int, input().split()))

unique = []

for i in range(len(arr)):
    if i == 0 or arr[i] != arr[i - 1]:
        unique.append(arr[i])

print(unique)
