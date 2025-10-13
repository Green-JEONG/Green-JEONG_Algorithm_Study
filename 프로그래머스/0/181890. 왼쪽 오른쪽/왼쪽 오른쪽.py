def solution(str_list):
    if 'l' not in str_list and 'r' not in str_list: # 주의: 둘 다 없을 때만이므로 or X
        return []
    
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i+1:]