a = input()
word = []

for i in range(len(a)):
    if a[i].isupper():
        word += a[i].lower()
    else:
        word += a[i].upper()
        
print("".join(word))