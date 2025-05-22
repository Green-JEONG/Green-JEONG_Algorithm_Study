from collections import Counter

s = input().upper()
    
mode = Counter(s).most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1]:
    print("?")
else:
    print(mode[0][0])