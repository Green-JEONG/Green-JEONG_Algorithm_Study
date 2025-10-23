def solution(s):
    result = []
    
    for word in s.split(' '):
        temp = ''
        for i in range(len(word)):
            if i % 2 == 1:
                temp += word[i].lower()
            else:
                temp += word[i].upper()
        result.append(temp)
        
    return ' '.join(result)