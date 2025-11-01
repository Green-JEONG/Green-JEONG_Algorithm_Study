-- 코드를 작성해주세요
SELECT
    YEAR(YM) AS YEAR, -- 그냥 연도만 추출
    ROUND(AVG(PM_VAL1), 2) AS PM10,
    ROUND(AVG(PM_VAL2), 2) AS `PM2.5`
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원' -- 문제에서 수원 지역 지정
GROUP BY YEAR -- 연도별로 묶어 평균 구하기
-- HAVING은 집계 결과에 조건 걸 때 사용
ORDER BY YEAR;