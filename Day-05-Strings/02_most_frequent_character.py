s = "banana"

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

most_char = None
most_count = 0

for ch in frequency:
    if frequency[ch] > most_count:
        most_count = frequency[ch]
        most_char = ch

print("Most frequent character:", most_char)
print("Frequency:", most_count)
