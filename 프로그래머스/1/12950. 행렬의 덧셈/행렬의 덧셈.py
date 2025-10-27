def solution(arr1, arr2):
    result = []
    
    for i in range(len(arr1)):
        row = [] # 현재 행의 덧셈 결과 저장
        
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        result.append(row)
    
    return result