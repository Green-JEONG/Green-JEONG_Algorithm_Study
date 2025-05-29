import sys

n = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))
    
nums = sorted(nums) # set은 정렬 불가능이므로, 리스트로 바꿔 정렬

print(*nums) # 리스트 언팩 후, 공백 출력