n = int(input())
scores = [int(input()) for _ in range(n)]

if n == 1:
    print(scores[0])
elif n == 2:
    print(scores[0] + scores[1])
else:
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    
    for i in range(3, n):
        dp[i] = max(
            dp[i - 2] + scores[i], # 한 칸 뛰어넘기
            dp[i - 3] + scores[i - 1] + scores[i] # 두 칸 뛰어넘고, 두 칸 연속 밟기
        )
        
    print(dp[-1]) # 마지막 계단