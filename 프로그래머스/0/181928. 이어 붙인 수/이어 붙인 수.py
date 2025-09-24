def solution(num_list):
    total_odd = ''
    total_even = ''
    for n in num_list:
        if n % 2:
            total_odd += str(n)
        else:
            total_even += str(n)
    return int(total_odd)+int(total_even)