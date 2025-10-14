def solution(myString):
    if 'a' in myString:
        myString = myString.replace('a', 'A')

    result = ""
    
    for ch in myString:
        if ch != 'A':
            result += ch.lower()
        else:
            result += ch
            
    return result