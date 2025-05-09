import sys

t = int(sys.stdin.readline().rstrip()) # 테스트 케이스 수

for _ in range(t):
    s = int(sys.stdin.readline().rstrip())    # 자동차 가격
    n = int(sys.stdin.readline().rstrip())    # 서로 다른 옵션 개수
    total_op = 0
    
    for _ in range(n):
        # q는 특정 옵션 개수, p는 해당 옵션 가격
        q, p = map(int, sys.stdin.readline().split())
        total_op += q * p
        
    print(s + total_op)