from itertools import combinations

n, m = map(int, input().split())

nums = [i for i in range(1, n + 1)]

result = combinations(nums, m)

# r은 튜플 형식
for r in result:
    # 튜플 괄호 없애고 공백 기준으로 숫자만 꺼내기
    print(*r)