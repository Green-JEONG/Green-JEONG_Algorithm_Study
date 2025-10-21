def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    myStr = myStr.split(' ')
    
    result = []
    
    for s in myStr:
        if s != '':
            result.append(s)
    
    if len(result) == 0:
        return ['EMPTY']
    return result