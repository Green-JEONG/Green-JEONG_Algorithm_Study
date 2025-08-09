def solution(A, B):
    if A == B:
        return 0
    s = A
    for k in range(1, len(A) + 1):  # k번 오른쪽 회전해보기
        s = s[-1] + s[:-1]
        if s == B:
            return k
    return -1