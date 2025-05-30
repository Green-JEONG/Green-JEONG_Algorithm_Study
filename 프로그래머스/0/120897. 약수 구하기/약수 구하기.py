def solution(n):
    measures = []
    for i in range(1, n + 1):
        if n % i == 0:
            measures.append(i)
    return measures