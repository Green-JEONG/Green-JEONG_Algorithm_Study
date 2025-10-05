ch = input()
string = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for s in string:
    if ch in s[2:4]:
        print(s)
        cnt += 1

print(cnt)