t = int(input())
a, b, c = 300, 60, 10

if t % 10 != 0:
    print(-1)
else:
    a_count = t // a
    t %= a    # t = t % a, 즉 a를 뺸 t의 갱신값이 다음으로 넘어가야
    
    b_count = t // b
    t %= b
    
    c_count = t // c
        # 넘어가야 할 t값 없으므로 X
    print(a_count, b_count, c_count)