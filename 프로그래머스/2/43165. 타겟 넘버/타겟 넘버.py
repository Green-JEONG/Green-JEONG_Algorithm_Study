from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)]) # 현재 합, 현재 인덱스
    count = 0 # target과 일치하는 경우의 수 세기
    
    while queue: # 큐가 빌 때까지 탐색(모든 경우 큐에 넣고, 큐에서 꺼내기 반복하며 확인)
        total, idx = queue.popleft()
        
        if idx == len(numbers):
            if total == target:
                count += 1
                
        else:
            queue.append((total + numbers[idx], idx+1))
            queue.append((total - numbers[idx], idx+1))
            
    return count