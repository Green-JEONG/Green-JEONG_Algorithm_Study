n, k = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

min_value = 0
for coin in reversed(coins): # coins[::-1] & sorted(coins, reverse=True)
    if k  >= coin:
        count = k // coin
        min_value += count
        k -= coin * count

print(min_value)