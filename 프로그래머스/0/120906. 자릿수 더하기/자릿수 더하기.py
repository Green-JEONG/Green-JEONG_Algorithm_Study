def solution(n):
    # total = 0
    # for i in str(n):
    #     total += int(i)
    # return total
    
    return sum(int(i) for i in str(n))