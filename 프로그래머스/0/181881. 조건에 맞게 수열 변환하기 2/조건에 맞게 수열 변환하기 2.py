def solution(arr):
    cnt = 0
    
    while True:
        new_arr = []
    
        for n in arr:
            if n >= 50 and n % 2 == 0:
                new_arr.append(n // 2)
            elif n < 50 and n % 2 != 0:
                new_arr.append(n * 2 + 1)
            else: # 그 외 나머지는 그대로 유지
                new_arr.append(n)
                
        if new_arr == arr:
            return cnt
        
        arr = new_arr
        cnt += 1