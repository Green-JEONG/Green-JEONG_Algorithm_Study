t = int(input())

for _ in range(t):
    word1, word2 = input().split()
    dist = []
    
    for a, b in zip(word1, word2):
        s1, s2 = ord(a) - 64, ord(b) - 64    # 알파벳 65부터 시작
        
        if s2 >= s1:
            sub = s2 - s1
        else:
            sub = (s2 + 26) - s1 # 알파벳은 26개
    
        dist.append(str(sub))
        
    print("Distances:", " ".join(dist))