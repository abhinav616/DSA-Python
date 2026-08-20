arr = list(map(int, input().split()))

sorted_arr = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_arr = False
        break

if sorted_arr:
    print("Sorted")
else:
    print("Not sorted")
