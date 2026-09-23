arr = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(arr)):
    current = arr[i]
    complement = target - current

    if complement in seen:
        print("Pair:", complement, current)
        break

    seen[current] = i
