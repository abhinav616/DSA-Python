arr = [1, 2, 2, 3, 1, 2, 4]

frequency = {}

for i in range(len(arr)):
    if arr[i] in frequency:
        frequency[arr[i]] += 1
    else:
        frequency[arr[i]] = 1

for i in frequency:
    if frequency[i] > 1:
        print(i)
