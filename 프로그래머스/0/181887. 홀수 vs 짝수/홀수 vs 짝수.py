def solution(num_list):
    odd_total = 0
    even_total = 0
    
    for i in range(len(num_list)):
        if i % 2 != 0:
            odd_total += num_list[i]
        else:
            even_total += num_list[i]
            
    return max(odd_total, even_total)