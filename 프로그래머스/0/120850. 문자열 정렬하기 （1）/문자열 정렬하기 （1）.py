def solution(my_string):
    nums = []
    for i in my_string:
        if i.isdecimal():
            nums.append(int(i))
    return sorted(nums)