def solution(myString):
    temp = myString.split('x')
    
    result = []
    for ch in temp:
        result.append(len(ch))
        
    return result