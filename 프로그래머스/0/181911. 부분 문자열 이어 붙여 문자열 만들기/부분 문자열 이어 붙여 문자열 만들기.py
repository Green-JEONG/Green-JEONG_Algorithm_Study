def solution(my_strings, parts):
    result = ""
    i = 0
    
    for s, e in parts:
        result += my_strings[i][s:e+1]
        i += 1
        
    return result