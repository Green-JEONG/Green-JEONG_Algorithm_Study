def solution(my_string, overwrite_string, s):
    # 세 부분으로 나누기
    # 교체 구간 교체 구간 '앞부분', 덮어쓸 문자열, 교체 구간 '뒷부분'
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]