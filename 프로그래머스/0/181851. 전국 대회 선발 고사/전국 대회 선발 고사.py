def solution(rank, attendance):
    students = []
    
    for i in range(len(rank)):
        if attendance[i]:
            students.append((rank[i], i)) # (등수, 인덱스 번호) 쌍으로 묶기
            
    # 등수 기준 오름차순 정렬
    students.sort()
    
    a, b, c = students[0][1], students[1][1], students[2][1]
    
    return 10000*a + 100*b + c