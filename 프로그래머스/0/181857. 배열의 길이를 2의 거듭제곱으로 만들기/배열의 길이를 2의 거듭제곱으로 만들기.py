def solution(arr):
    power = 1 # 2**0 = 2^0부터 시작
    
    while power < len(arr): # power가 정수 배열 길이보다 커지는 순간에 반복문 빠져나옴 (조건 적용되지 않고)
        power *= 2
        
    while len(arr) < power:
        arr.append(0)
        
    return arr