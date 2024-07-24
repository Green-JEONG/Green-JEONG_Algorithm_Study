# 마지막 줄이 "0 0"으로 끝나는 것은 더 이상 비교하지 않겠다는 의미
while True:
    # 두 숫자 입력받고, 정수형으로 변환
    # .split() 메서드: 공백을 기준으로 나누어 리스트 생성
    # map() 함수: 두 번째 인자(리스트)의 각 요소에, 첫 번째 인자(함수) 적용 = 문자열 리스트를 정수 리스트로 변환
    a, b = map(int, input().split())

    # 입력이 0 0이면 반복문 종료
    if a == 0 and b == 0:
        break
    
    if a > b:
        print("Yes")
    else:
        print("No")
