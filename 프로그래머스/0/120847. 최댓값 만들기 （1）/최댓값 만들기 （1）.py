def solution(numbers):
    asc_numbers = sorted(numbers)
    return asc_numbers[-1] * asc_numbers[-2]