def solution(my_string, index_list):
    result = ""
    
    for x in index_list:
        result += my_string[x]
        
    return result