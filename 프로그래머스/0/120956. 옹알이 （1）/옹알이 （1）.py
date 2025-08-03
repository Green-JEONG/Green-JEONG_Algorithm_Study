def solution(babbling):
    sound = ['aya', 'ye', 'woo', 'ma']
    count = 0
    
    for b in babbling:
        temp = b
        for s in sound:
            if s in temp:
                temp = temp.replace(s, ' ', 1)
        
        if temp.strip() == '':
            count += 1
            
    return count