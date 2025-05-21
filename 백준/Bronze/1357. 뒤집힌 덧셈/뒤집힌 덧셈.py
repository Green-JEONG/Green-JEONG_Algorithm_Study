x, y = map(int, input().split())

reverse_x = int(str(x)[::-1])
reverse_y = int(str(y)[::-1])

plus = reverse_x + reverse_y
reverse_plus = str(plus)[::-1]

print(int(reverse_plus))