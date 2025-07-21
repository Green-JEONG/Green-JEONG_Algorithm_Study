def solution(array):
    count = 0
    for n in array:
        for ch in str(n):
            if ch == '7':
                count += 1
        
    return count