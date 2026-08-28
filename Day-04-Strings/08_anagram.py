s1 = "listen"
s2 = "silent"

frequency1 = {}
frequency2 = {}

for ch in s1:
    if ch in frequency1:
        frequency1[ch] += 1
    else:
        frequency1[ch] = 1

for ch in s2:
    if ch in frequency2:
        frequency2[ch] += 1
    else:
        frequency2[ch] = 1

if frequency1 == frequency2:
    print("Anagram")
else:
    print("Not Anagram")
