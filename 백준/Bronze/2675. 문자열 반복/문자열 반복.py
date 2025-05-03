T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R) # 반복 횟수만 정수
    
    P = '' # 문자열 변수 초기화
    for char in S:
        P += char * R # 한 문자 R번 반복
        
    print(P)