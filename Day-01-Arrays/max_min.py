arr = list(map(int, input().split()))

maximum = arr[0]

for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

print("Maximum:", maximum)

minimum = arr[0]

for i in range(len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]

print("Minimum:", minimum)
