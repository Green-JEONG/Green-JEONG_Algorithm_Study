def solution(arr, queries):
    for s, e, k in queries: # 각 쿼리마다
        for i in range(s, e+1): # s~e 범위의 인덱스만 확인
                if i % k == 0:
                    arr[i] += 1
                
    return arr