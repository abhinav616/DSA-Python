arr = list(map(int, input().split()))

even = []
odd = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

print("Even:", even)
print("Even count:", len(even))

print("Odd:", odd)
print("Odd count:", len(odd))
