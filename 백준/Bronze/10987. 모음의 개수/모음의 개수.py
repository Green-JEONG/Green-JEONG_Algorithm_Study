vowel = ['a', 'e', 'i', 'o', 'u']

s = input()

total = 0
for i in s:
    if i in vowel:
        total += 1
        
print(total)