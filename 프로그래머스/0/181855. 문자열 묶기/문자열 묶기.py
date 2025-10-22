def solution(strArr):
    lengths = {}
    
    for s in strArr:
        if len(s) not in lengths:
            lengths[len(s)] = 1 # 딕셔너리에서는 [] 안 값은 '키', 딕셔너리는 순서 X
        else:
            lengths[len(s)] += 1
            
    return max(lengths.values())