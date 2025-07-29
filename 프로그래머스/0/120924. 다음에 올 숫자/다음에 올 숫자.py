def solution(common):
    a = common[0]
    b = common[1]
    c = common[2]
    
    # 등차수열
    if b - a == c - b:
        d = b - a
        return common[-1] + d # 마지막 수에 공차(d) 더하기
    # 등비수열
    else:
        r = b // a
        return common[-1] * r # 마지막 수에 공비(r) 곱하기