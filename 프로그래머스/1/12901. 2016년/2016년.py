def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    total_days = 0
    for i in range(a-1):
        total_days += days[i]
    total_days += b
    
    return week[(total_days - 1) % 7] # 인덱스는 0부터 시작하는데 total_days는 1부터 시작하니 1 빼주고 일주일 나눠줘야 함