def solution(arr, queries):
    for i, j in queries: # 각 쿼리 i, j 바로 꺼냄
        arr[i], arr[j] = arr[j], arr[i] # swap(값 교환)
            
    return arr