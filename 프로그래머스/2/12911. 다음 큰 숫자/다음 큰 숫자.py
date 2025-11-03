def solution(n):
    target = bin(n).count('1')
    
    while True:
        n += 1
        if bin(n).count('1') == target:
            return n # 조건이 충족되면 종료 (break와 동일) = 조건 충족될 때까지 반복