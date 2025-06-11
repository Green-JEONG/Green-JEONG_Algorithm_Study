t = int(input())

# DP(동적 계획법): 1,2,3 조합으로 정수 만드는 경우의 수 구하기
# 정수 n을 1,2,3 합으로 만드는 방법의 수 = (n-1) + (n-2) + (n-3) 각각 만드는 방법 수 합
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 4 ~ 11까지 미리 계산
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])