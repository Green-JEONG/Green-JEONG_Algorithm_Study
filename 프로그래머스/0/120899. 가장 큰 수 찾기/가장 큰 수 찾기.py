def solution(array):
    max_value = max(array)
    i_max = array.index(max_value)
    
    return [max_value, i_max]