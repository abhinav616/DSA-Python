arr = list(map(int, input().split()))
target = int(input("Enter target: "))

left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total > target:
        right -= 1

    elif total < target:
        left += 1

    else:
        print("Pair found:", arr[left], arr[right])
        break
else:
    print("No pair found")
