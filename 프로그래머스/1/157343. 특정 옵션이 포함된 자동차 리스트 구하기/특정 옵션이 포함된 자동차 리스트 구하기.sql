-- 코드를 입력하세요
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%' -- 와일드카드 문자 '%' 사용해서 앞뒤에 뭐가 있든 상관없이, 이 단어가 포함돼 있으면 찾기
ORDER BY CAR_ID DESC;