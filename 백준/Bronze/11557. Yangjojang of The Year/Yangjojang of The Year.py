t = int(input())

for _ in range(t):
    n = int(input())
    max_school = ""
    max_alcohol = -1    # 술 소비량은 항상 0 이상이므로 소비량이 0일 경우 오류 방지
    
    for _ in range(n):
        s, l = input().split()
        l = int(l)
        if l > max_alcohol:
            max_school = s
            max_alcohol = l
        
    print(max_school)