def solution(myString):
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    newString = []
    for i in myString:
        if i in alph:
            newString.append("l")
        else:
            newString.append(i)
            
    return ''.join(newString)