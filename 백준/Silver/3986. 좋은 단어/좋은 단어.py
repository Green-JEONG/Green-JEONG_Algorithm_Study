n = int(input())

count = 0

for _ in range(n):
    word = input().rstrip()
    stack = []
    
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
            
    if not stack:
        count += 1
        
print(count)