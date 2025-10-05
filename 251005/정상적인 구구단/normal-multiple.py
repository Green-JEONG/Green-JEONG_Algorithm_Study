n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f'{i} * {j} = {i*j}', end='')
        if j != n: # 마지막이 아닐 때만 콤마+공백 출력
            print(', ', end='')
    print()