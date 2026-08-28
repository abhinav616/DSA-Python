vowels = ['a', 'e', 'i', 'o', 'u']

s = "hello"

vowel = 0
consonant = 0

for i in range(len(s)):
    if s[i] in vowels:
        vowel += 1
    else:
        consonant += 1

print("Vowels:", vowel)
print("Consonants:", consonant)
