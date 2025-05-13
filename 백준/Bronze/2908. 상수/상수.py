a, b = map(int, input().split())

a1 = str(a)[::-1]
a2 = str(b)[::-1]

print(max(int(a1), int(a2)))