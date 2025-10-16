-- 코드를 입력하세요
SELECT MCDP_CD AS 진료과코드, COUNT(*) AS `5월예약건수` -- 숫자로 시작 불가, 문자나 따옴표로 감싸는 것과 동일
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY 진료과코드
ORDER BY `5월예약건수`, 진료과코드;