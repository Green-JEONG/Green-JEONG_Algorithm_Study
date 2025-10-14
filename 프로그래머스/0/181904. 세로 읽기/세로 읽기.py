def solution(my_string, m, c):
    result = ""
    
    for i in range(c, len(my_string)+1, m):
        result += my_string[i-1]
    return result