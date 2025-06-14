import sys
input = sys.stdin.readline

n, m = map(int, input().split())

unheard = {input().strip() for _ in range(n)}
unseen = {input().strip() for _ in range(m)}
        
intersection = sorted(unheard & unseen)

print(len(intersection))
print('\n'.join(intersection))