def solution(code):
    ret = ''
    mode = 0
    
    for idx, ch in enumerate(code): # ch == code[idx]
        if ch == '1': # mode의 공통 조건
            mode = 1 - mode
        else:
            if mode == 0 and idx % 2 == 0:
                ret += ch
            elif mode == 1 and idx % 2 == 1:
                ret += ch

    return ret if ret else 'EMPTY'