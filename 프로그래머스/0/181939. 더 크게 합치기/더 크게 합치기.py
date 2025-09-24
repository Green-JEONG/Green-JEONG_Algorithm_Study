def solution(a, b):
    asc_s = int(str(a) + str(b))
    desc_s = int(str(b) + str(a))
    return desc_s if asc_s < desc_s else asc_s