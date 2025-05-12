def solution(a, b):
    string = str(a) + str(b)
    num = 2 * a * b
    return max(int(string), num)