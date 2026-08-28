s = "programming"

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in frequency:
    if frequency[ch] > 1:
        print(ch)
