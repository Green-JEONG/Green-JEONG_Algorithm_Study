def solution(s, skip, index):
    skip = set(skip)
    result = []
    
    for ch in s:
        cur = ch
        cnt = 0
        
        while cnt < index:
            cur = chr((ord(cur) - ord('a') + 1) % 26 + ord('a'))
            if cur not in skip:
                cnt += 1
                
        result.append(cur)
        
    return ''.join(result)