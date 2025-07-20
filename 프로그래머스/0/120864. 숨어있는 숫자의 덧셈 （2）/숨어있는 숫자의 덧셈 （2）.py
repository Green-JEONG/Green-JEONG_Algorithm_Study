def solution(my_string):
    temp = ''
    nums = []
    
    for ch in my_string:
        if ch.isdigit():
            temp += ch
        else:
            if temp != '':
                nums.append(int(temp))
                temp = ''
                
    if temp != '':
        nums.append(int(temp))
    
    return sum(nums)