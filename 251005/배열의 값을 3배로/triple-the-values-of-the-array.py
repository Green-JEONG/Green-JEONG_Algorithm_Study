matrix = [list(map(int, input().split())) for _ in range(3)]

new_matrix = [
    [element * 3 for element in row]
    for row in matrix
]

for row in new_matrix:
    print(' '.join(map(str, row)))