t = int(input())

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0] # f(0): 0 한번
dp[1] = [0, 1] # f(1): 1 한번

for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for _ in range(t):
    n = int(input())
    
    print(dp[n][0], dp[n][1])