def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1): # 마지막 원소 직전까지만 확인하기 위해 1 빼주기
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True # 모든 비교 끝난 뒤 실행