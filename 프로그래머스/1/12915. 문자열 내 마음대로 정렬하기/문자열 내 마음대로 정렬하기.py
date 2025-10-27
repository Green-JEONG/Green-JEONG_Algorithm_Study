def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x)) # 각 단어에서 인덱스 n번 글자 꺼내기 + 그 글자가 같으면 두 번째 튜플 사전순 출력
    
    return strings
    