k = int(input())

for i in range(k):
    nums = list(map(int, input().split()))
    n = nums[0]
    
    scores = sorted(nums[1:], reverse=True)
    
    max_score = scores[0]
    min_score = scores[-1]
    
    gaps = [scores[i] - scores[i + 1] for i in range(n - 1)] # N개에서 2개씩 비교 시, 1만 빼줌
    largest_gap = max(gaps)
        
    print("Class", i + 1)
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")