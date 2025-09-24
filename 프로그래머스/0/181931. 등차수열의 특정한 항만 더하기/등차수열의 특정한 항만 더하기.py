def solution(a, d, included):
    total = 0
    for i, flag in enumerate(included):
        term = a + i * d # 등차'수열의' n'항'
        if flag: # included[i]가 True면
            total += term
    return total