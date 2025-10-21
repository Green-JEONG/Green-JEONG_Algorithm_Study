def solution(arr, flag):
    result = []
    
    for i in range(len(arr)):
        if flag[i]:
            for _ in range(arr[i]*2): # arr[i] * 2번 추가
                result.append(arr[i])
        else:
            for _ in range(arr[i]):
                result.pop()
    
    return result