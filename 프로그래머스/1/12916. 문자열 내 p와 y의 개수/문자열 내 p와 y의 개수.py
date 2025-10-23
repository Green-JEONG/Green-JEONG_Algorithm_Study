def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y') # 둘 다 없으면 0 == 0이므로 True 처리