def solution(arr):
    
    if len(arr) > len(arr[0]):
        for i in range(len(arr)):
            while len(arr[i]) < len(arr): # 현재 행 길이 기준으로 비교해야 함
                arr[i].append(0)
                
    elif len(arr) < len(arr[0]):
        while len(arr) < len(arr[0]):
            arr.append([0] * len(arr[0]))
                
    return arr