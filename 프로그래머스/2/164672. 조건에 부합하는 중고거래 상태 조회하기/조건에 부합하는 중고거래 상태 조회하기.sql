-- 코드를 입력하세요
SELECT BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    CASE
        WHEN STATUS = 'SALE' THEN '판매중' -- CASE 문의 THEN 뒤는 '값'을 반환하므로 문자열 데이터를 괄호로 감싸야 함
        WHEN STATUS = 'RESERVED' THEN '예약중'
        ELSE '거래완료'
    END AS STATUS -- 컬럼명은 식별자로 취급
FROM USED_GOODS_BOARD
WHERE DATE_FORMAT(CREATED_DATE, '%Y-%m-%d') = '2022-10-05'
ORDER BY BOARD_ID DESC;