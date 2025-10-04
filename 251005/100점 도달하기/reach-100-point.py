n = int(input())
s = ""
while n <= 100:
    if n >= 90:
        s += 'A'
    elif n >= 80:
        s += 'B'
    elif n >= 70:
        s += 'C'
    elif n >= 60:
        s += 'D'
    else:
        s += 'F'
    n += 1
print(' '.join(s))