def solution(myString, pat):
    myString = myString.replace('A', 'X')
    myString = myString.replace('B', 'A')
    myString = myString.replace('X', 'B')
    
    return int(pat in myString)