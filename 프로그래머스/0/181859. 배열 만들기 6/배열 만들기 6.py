def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk: # len(stk) == 0
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
        i += 1 # 공통 조건
            
    if not stk:
        return [-1]
    return stk