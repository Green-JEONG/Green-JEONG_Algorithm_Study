def solution(l, r):
    arr = []
    
    for i in range(l, r+1):
        if all(ch in '05' for ch in str(i)):
            arr.append(i)

    return arr if arr else [-1]