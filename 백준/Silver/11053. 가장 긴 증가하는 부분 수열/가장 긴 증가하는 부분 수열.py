n = int(input())
a = list(map(int, input().split()))

dp = [1] * n # 초기 1 세팅 (부터 시작)

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1) # 이어 붙일 수 있으면 길이 하나 늘어남
            
print(max(dp))