def solution(cipher, code):
    s = []
    for i in range(len(cipher)):
        if (i + 1) % code == 0:
            s.append(cipher[i])
    return ''.join(s)