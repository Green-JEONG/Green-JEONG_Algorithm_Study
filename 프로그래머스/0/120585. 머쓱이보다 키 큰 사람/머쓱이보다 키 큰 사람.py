def solution(array, height):
    # total = 0
    # for i in array:
    #     if i > height:
    #         total += 1
    # return total
    
    # return len([i for i in array if i > height])

    return sum(1 for i in array if i > height)