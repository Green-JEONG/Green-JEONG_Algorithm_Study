t = int(input())

for i in range(t):
    n = bin(int(input()))
    binary = n[::-1]
    
    for i in range(len(binary)):
        if binary[i] == '1':
            print(i, end=' ')