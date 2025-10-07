def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp = [x for x in arr[s:e+1] if x > k]
        
        if temp: # 그런 값이 있다면 (하나 수 반복시마다)
            answer.append(min(temp)) # 그 중 최소값 찾기
        else:
            answer.append(-1)
            
    return answer