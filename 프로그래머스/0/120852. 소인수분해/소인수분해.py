def solution(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:       # i로 나누어 떨어지면
            factors.append(i)
            while n % i == 0:  # 같은 소인수는 계속 나누기
                n //= i
        i += 1
    return factors