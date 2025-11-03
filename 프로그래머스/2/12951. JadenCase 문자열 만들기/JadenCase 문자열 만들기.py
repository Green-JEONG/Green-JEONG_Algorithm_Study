def solution(s):
    # 일반 split()는 연속 공백 무시
    # '': 빈 문자열 (아무것도 없음), 길이 0
    # ' ': 공백 문자열 (공백 1칸 있음), 길이 1
    return ' '.join(
        ch.capitalize() if ch else ""
        for ch in s.split(' ')
    )