import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ps = input()
    count = 0
    
    for i in ps:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count < 0:
                print("NO")
                break
    else:    # for문이 break 없이 끝까지 실행되면 실행
        if count == 0:
            print("YES")
        else:
            print("NO")          