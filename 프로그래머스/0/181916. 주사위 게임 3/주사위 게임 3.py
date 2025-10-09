from collections import Counter # 각 숫자가 몇 번 나왔는지 세줌

def solution(a, b, c, d):
    nums = [a, b, c, d]
    count = Counter(nums) # 예: Counter({4: 3, 1: 1})
    
    keys = list(count.keys())
    values = list(count.values())
    
    if len(count) == 1:
        return 1111 * a
        
    elif 3 in values:
        p = keys[values.index(3)]
        q = keys[values.index(1)]
        return  (10 * p + q) ** 2
        
    elif values.count(2) == 2:
        p, q = keys # 리스트나 튜플 요소를 한 번에 여러 변수에 나눠담는 '언패킹' 가능
        return (p + q) * abs(p - q)
        
    elif len(count) == 3:
        p = keys[values.index(2)]
        q, r = [k for k in keys if k != p]
        return q * r
        
    else:
        return min(nums)
        