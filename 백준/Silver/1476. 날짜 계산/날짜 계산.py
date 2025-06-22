e, s, m = map(int, input().split())

year = 1
while True:
    if (year - 1) % 15 == e - 1 and (year - 1) % 28 == s - 1 and (year - 1) % 19 == m - 1:
        print(year)
        break
    year += 1