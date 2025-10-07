n = int(input())

for i in range(n):
    if i % 2 == 0: # 행, 열도 인덱스 0부터 시작
        for j in range(1, n+1):
            print(j, end='')
    else:
        for j in range(n, 0, -1): # 인덱스 거꾸로 4, 3, 2, 1
            print(j, end='')
    print()