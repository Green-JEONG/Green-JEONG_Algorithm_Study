def solution(numbers):
    result = sorted(numbers)[-1] * sorted(numbers)[-2]
    return result