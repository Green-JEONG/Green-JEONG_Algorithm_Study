from itertools import combinations

def solution(numbers):
    result = set()

    for i in combinations(numbers, 2):
        result.add(sum(i))
        
    return sorted(result)