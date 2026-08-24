arr = list(map(int, input().split()))

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

left = int(input("Enter left index: "))
right = int(input("Enter right index: "))

if left == 0:
    total = prefix[right]
else:
    total = prefix[right] - prefix[left - 1]

print("Range sum:", total)
