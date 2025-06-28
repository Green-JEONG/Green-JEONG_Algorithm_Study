n = int(input())
length = 0
digit = 1 # 현재 자릿수
start = 1

while start * 10 <= n:
    end = start * 10 - 1 # 끝자리가 9
    count = end - start + 1
    length += count * digit
    digit += 1
    start *= 10 # 다음 범위로 넘어감
    
# 남은 구간 처리 (start ~ n)
count = n - start + 1
length += count * digit

print(length)