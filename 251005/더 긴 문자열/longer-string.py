s, n = input().split()

if len(s) > len(n):
    print(s, len(s))
elif len(s) < len(n):
    print(n, len(n))
else:
    print('same')