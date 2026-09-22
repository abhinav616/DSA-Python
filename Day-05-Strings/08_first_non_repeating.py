s = "aabbcddee"

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in s:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break
