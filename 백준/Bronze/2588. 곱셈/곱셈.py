# 산술 연산자 풀이
a = int(input())
b = int(input())

print(a * (b % 10))    # 백의 자리 수 b를 10으로 나눈 나머지
print(a * (b % 100 // 10))    # 백의 자리 수 b를 100으로 나눈 나머지에 10으로 나눈 몫
print(a * (b // 100))    # 백의 자리 수 b를 100로 나눈 몫
print(a * b)
