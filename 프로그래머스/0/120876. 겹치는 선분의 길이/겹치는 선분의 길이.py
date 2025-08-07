def solution(lines):
    coords = [0] * 201
    
    for start, end in lines:
        for i in range(start + 100, end + 100):
            coords[i] += 1
    
    return sum(1 for x in coords if x >= 2)