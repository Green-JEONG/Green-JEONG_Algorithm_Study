# GCD: 최대공약수
from math import gcd

t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))
    n = numbers[0] # 첫 번째 숫자 = 테스트 수 개수
    nums = numbers[1:] # 나머지 숫자 = n개의 수
    
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += gcd(nums[i], nums[j])
            
    print(total)