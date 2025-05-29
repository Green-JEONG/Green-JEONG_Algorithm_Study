import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    order = sys.stdin.readline().rstrip()
    
    if "push" in order:
        _, value = order.split()
        stack.append(int(value))
    elif order == "pop":
        if stack:
            print(stack.pop()) # 스택은 젤 최신이 맨 위(=마지막 값)
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        print(0 if stack else 1)
    elif order == "top":
        if stack:
            print(stack[-1]) # 가장 위 = 가장 뒤(=맨마지막 값)
        else:
            print(-1)
        