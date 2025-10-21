def solution(myString):
    myString = myString.strip('x')
    
    result = []
    for ch in myString.split('x'):
        if ch != '':
            result.append(ch)
            
    return sorted(result)