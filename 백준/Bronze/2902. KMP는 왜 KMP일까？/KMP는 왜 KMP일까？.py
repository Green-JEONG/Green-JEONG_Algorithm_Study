s = input()

result = []
for i in s:
    if i.isupper():
        result.append(i)
        
print("".join(result))