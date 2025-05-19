t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    
    even = []
    even_sum = 0
    for n in nums:
        if n % 2 == 0:
            even.append(n)
            even_sum += n
    
    
    print(even_sum, min(even))