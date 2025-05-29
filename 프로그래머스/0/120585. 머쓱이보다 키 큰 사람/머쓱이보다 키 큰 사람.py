def solution(array, height):
    total = 0
    for h in array:
        if h > height:
            total += 1
    return total