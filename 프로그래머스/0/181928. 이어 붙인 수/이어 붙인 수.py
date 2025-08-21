def solution(num_list):
    odd_str = ""
    even_str = ""
    
    for n in num_list:
        if n % 2:
            odd_str += str(n)
        else:
            even_str += str(n)
    
    return int(odd_str) + int(even_str)