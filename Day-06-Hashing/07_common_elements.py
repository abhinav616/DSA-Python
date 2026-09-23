
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

set1 = set(arr1)

for num in arr2:
    if num in set1:
        print(num)
