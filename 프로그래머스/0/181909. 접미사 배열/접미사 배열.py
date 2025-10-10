def solution(my_string):
    result = []
    
    for i in range(len(my_string)):
        result.append(str(my_string[i:]))
        i += 1
        
    return sorted(result)