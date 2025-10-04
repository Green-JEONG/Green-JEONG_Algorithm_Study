s = input()

new_s = list(s)
new_s[1] = 'a'
new_s[-2] = 'a'

print(''.join(map(str, new_s)))