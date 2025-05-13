a = int(input())
b = int(input())
c = int(input())

multi = a * b * c
multi_str = str(multi)
multi_list = list(multi_str)

for i in range(10):
    print(multi_list.count(str(i)))