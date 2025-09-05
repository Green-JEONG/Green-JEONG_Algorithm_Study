def solution(num_list):
    from math import prod
    return 1 if prod(num_list) < sum(num_list) ** 2 else 0