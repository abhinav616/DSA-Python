arr = [4, 5, 1, 2, 1, 4, 5]

frequency = {}

for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for i in arr:
    if frequency[i] == 1:
        print(i)
        break
