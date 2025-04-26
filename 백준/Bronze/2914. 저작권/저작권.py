a, i = map(int, input().split())

'''
/ A = i (단, 올림)
i - 1 < X / A <= i
(i - 1) * A < X <= i * A

X / A < i
X < i * A
X < 24 * 38
X < 912

X / A > i - 1
X > (i - 1) * A
X > 23 * 38
X > 874
'''

print((i - 1) * a + 1)