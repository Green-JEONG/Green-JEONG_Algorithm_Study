def solution(arr):
    result = []
    
    for n in arr:
        for _ in range(n): # n번 반복 (숫자 n을 n번 추가)
            result.append(n)
        
    return result