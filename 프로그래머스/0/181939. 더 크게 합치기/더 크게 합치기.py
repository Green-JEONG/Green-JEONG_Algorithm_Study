def solution(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    return max(int(str1), int(str2))