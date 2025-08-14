def solution(dots):
    def slope(a, b):
        return (b[1] - a[1]) / (b[0] - a[0])  # 기울기
    
    # 세 가지 조합만 비교
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    return 0