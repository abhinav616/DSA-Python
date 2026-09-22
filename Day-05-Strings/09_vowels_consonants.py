s = "education"

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0
consonant_count = 0

for ch in s:
    if ch in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
