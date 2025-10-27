from itertools import combinations

def solution(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1): # math.sqrt(n)과 동일
            if n % i == 0:
                return False
        return True
    
    cnt = 0
    
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            cnt += 1
    
    return cnt