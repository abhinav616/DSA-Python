s = "banana"

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

least_char = None
least_count = None

for ch in frequency:
    if least_count is None or frequency[ch] < least_count:
        least_count = frequency[ch]
        least_char = ch

print("Least frequent character:", least_char)
print("Frequency:", least_count)
