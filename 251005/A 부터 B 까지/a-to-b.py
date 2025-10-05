a, b = map(int, input().split())
answer = [a]
while a <= b:
    if a % 2 == 1:
        a *= 2    
    else:
        a += 3
    if a > b:
        break
    answer.append(a)
print(' '.join(map(str, answer)))
