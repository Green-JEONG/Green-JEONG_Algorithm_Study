while True:
    try: # 입력을 받는 부분, 입력 없을 때 예외 처리
        A, B = map(int, input().split())
        print(A+B)
    except: # 입력이 없을 때 예외 (에러 발생 시 루프 종료)
        break