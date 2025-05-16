while 1:
    a, b, c = map(int, input().split())
    
    if a == b == c == 0:
        break
        
    nums = sorted([a, b, c])
        
    if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
        print("right")
    else:
        print("wrong")