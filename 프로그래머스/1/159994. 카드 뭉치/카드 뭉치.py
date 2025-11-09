def solution(cards1, cards2, goal):
    # 핵심: 두 개의 카드 뭉치 순서 유지한 채로 goal 단어 배열 생성 가능한지 확인
    # 1) 두 카드 뭉치 단어 순서 유지
    # 2) 한 번 뽑은 카드 다시 사용 X
    # 3) 사용 안 한 카드 건너 뛸 수 X
    
    i, j = 0, 0 # 카드 cards1, cards2의 현재 위치
    
    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            i += 1
        elif j < len(cards2) and word == cards2[j]:
            j += 1
        else:
            return "No"
        
    return "Yes"