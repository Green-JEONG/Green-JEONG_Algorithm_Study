def solution(s):
    last_ch = {}
    result = []
    
    for i, ch in enumerate(s):
        if ch in last_ch:
            result.append(i - last_ch[ch]) # 현재 위치 - 이전 위치
        else:
            result.append(-1)
        last_ch[ch] = i # 현재 위치 기록(갱신)
        
    return result
        