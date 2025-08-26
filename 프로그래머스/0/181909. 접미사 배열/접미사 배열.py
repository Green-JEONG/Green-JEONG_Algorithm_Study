def solution(my_string):
    suffi = []
    for i in range(len(my_string)):
        suffi.append(my_string[i:])
    
    return sorted(suffi)