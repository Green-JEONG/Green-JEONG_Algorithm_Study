N, X = map(int, input().split())
A = list(map(int, input().split()))    # 리스트 안 문자열을 int로 만든 map 객체를 진짜 list로 바꾸기
  
for i in A:    # A 안에서
    if i < X:    # X보다 작은 값 찾기
        print(i, end=' ')    # 줄바꿈을 공백으로 바꾸기