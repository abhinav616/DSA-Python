A = list(map(int, input("Enter first sorted array: ").split()))
B = list(map(int, input("Enter second sorted array: ").split()))

i = 0
j = 0
result = []

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1

while i < len(A):
    result.append(A[i])
    i += 1

while j < len(B):
    result.append(B[j])
    j += 1

print("Merged array:", result)
