answer = []
while True:
    n = int(input())
    if n == 25:
        answer.append('Good')
        break
    elif n < 25:
        answer.append('Higher')
    else:
        answer.append('Lower')
print('\n'.join(map(str, answer)))