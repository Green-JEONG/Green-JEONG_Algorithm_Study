n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
min = price[0] # 초기때 가장 싼 기름값

for i in range(n - 1): # 도로 개수
    if price[i] < min:
        min = price[i]
        
    total += min * distance[i]
    
print(total)