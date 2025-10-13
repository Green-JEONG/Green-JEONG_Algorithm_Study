def solution(arr):
    if 2 not in arr:
        return [-1]
    
    first = arr.index(2)
    last = len(arr) - 1 - arr[::-1].index(2) # 뒤집힌 배열에서 찾은 인덱스의 원래 배열 위치 인덱스 추출 => 원래 인덱스 = (배열 길이 - 1) - 뒤집은 배열에서의 인덱스
    
    return arr[first:last+1]