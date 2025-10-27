def solution(n):
    for x in range(1, n+1):
        if x**2 == n:
            return (x+1)**2
    return -1 # for문 전체를 다 돌고 나서도 못 찾았을 때 -1 리턴