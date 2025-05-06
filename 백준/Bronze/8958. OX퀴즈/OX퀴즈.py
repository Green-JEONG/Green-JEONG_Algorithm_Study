n = int(input())

for _ in range(n):
    str = input()
    score = 0    # 총 점수
    consec = 0    # 연속 O 점수
    
    for ch in str:
        if ch == "O":
            consec += 1
            score += consec
        else:
            consec = 0    # X 나올 시, 연속 끊기
       
    print(score)