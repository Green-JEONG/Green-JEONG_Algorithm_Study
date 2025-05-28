import sys

n = int(sys.stdin.readline())

words = set()
for _ in range(n):
    words.add(sys.stdin.readline().rstrip())
    
# sorted_words = sorted(words, key=lambda x: (len(x), x))
words = list(words) # set(집합)에서 사용하는 메서드를 list로 변경
words.sort() # 사전 순 (안정 정렬이라, 뒤에 하는 기준이 우선 적용)
words.sort(key=len) # 길이 순

for word in words:
    print(word)