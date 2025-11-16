def solution(ingredient):
    stack = []
    cnt = 0
    
    for i in ingredient:
        stack.append(i)
        
        # 스택에 재료가 4개 이상 쌓인 동시에, 마지막 4개가 [빵-야채-고기-빵]일 때,
        if stack[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4):
                stack.pop()
                
    return cnt