arr = list(map(int, input().split()))

n = len(arr)

for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

print("The reversed array is:", arr)
