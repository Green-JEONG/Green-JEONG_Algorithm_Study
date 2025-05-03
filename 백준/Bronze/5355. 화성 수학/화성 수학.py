T = int(input())

for _ in range(T):
    data = input().split()
    num = float(data[0])
    
    for i in data[1:]:
        if i == "@":
            num *= 3
        elif i == "%":
            num += 5
        elif i == "#":
            num -= 7
            
    print(f"{num:.2f}")