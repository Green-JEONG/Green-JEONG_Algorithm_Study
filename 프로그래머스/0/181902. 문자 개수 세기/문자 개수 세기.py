def solution(my_string):
    result = []
    
    for i in range(26):
        result.append(my_string.count(chr(i+65)))
    for i in range(26):
        result.append(my_string.count(chr(i+97)))
        
    return result