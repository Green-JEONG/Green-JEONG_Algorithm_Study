# x축 or y과 평행
# x좌표 or y좌표 두번 나와야

x = y = 0

for _ in range(3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b
        
print(x, y)