def solution(str1, str2):

    result = ""
    
    min_len = min(len(str1), len(str2))
    
    for i in range(min_len):
        result += str1[i] + str2[i]
        
    return result