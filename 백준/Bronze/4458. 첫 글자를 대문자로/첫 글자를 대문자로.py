n = int(input())

for _ in range(n):
    s = input()
    new_s = s[0].upper() + s[1:]
    
    print(new_s)