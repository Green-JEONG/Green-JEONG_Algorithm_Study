def solution(s):
    nums = []
    for i in s.split():
        if i == 'Z':
            if nums:
                nums.pop()
        else:
            nums.append(int(i))
    return sum(nums)