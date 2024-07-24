from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))  # 한국 표준시 (KST) 설정
today = datetime.now(KST)  # 현재 한국 표준시로 시간 가져오기
print(today.strftime("%Y-%m-%d"))  # YYYY-MM-DD 형식으로 출력