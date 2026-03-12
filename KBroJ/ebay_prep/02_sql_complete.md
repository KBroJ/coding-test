# SQL 완전 정리
> MySQL / 프로그래머스 / 30분 목표

---

## 문제 풀이 순서 (항상 이 순서로)

```
1. 테이블 구조 파악 (어떤 컬럼이 있나)
2. 출력 컬럼명 확인 (AS 별칭 필요한지)
3. 필터 조건 (WHERE, HAVING)
4. 그룹핑 필요? (GROUP BY)
5. 조인 필요? (JOIN)
6. 정렬 (ORDER BY)
7. 개수 제한? (LIMIT)
```

---

## 핵심 패턴 1: GROUP BY + 집계함수 ★★★

**데모 문제 유형. 가장 자주 나옴.**

```sql
-- 지점별 총 급여, 지점ID 오름차순
SELECT BRANCH_ID, SUM(SALARY) AS TOTAL
FROM EMPLOYEES
GROUP BY BRANCH_ID
ORDER BY BRANCH_ID;

-- 집계함수 종류
SUM(col)    -- 합계
AVG(col)    -- 평균
COUNT(*)    -- 행 수 (NULL 포함)
COUNT(col)  -- 해당 컬럼 NULL 제외 행 수
MAX(col)    -- 최댓값
MIN(col)    -- 최솟값
```

---

## 핵심 패턴 2: WHERE vs HAVING

```sql
-- WHERE: GROUP BY 전 필터 (개별 행)
-- HAVING: GROUP BY 후 필터 (그룹 집계)

SELECT BRANCH_ID, SUM(SALARY) AS TOTAL
FROM EMPLOYEES
WHERE SALARY >= 200          -- 개별 행 필터 먼저
GROUP BY BRANCH_ID
HAVING SUM(SALARY) >= 500    -- 그룹 집계 후 필터
ORDER BY BRANCH_ID;
```

---

## 핵심 패턴 3: JOIN ★★★

```sql
-- INNER JOIN: 양쪽 다 있는 것만
SELECT e.NAME, d.DEPT_NAME
FROM EMPLOYEES e
INNER JOIN DEPARTMENT d ON e.BRANCH_ID = d.ID;

-- LEFT JOIN: 왼쪽 기준, 오른쪽 없으면 NULL
SELECT e.NAME, d.DEPT_NAME
FROM EMPLOYEES e
LEFT JOIN DEPARTMENT d ON e.BRANCH_ID = d.ID;

-- 기억법
-- INNER: 교집합 (A ∩ B)
-- LEFT:  왼쪽 전체 + 오른쪽 매칭 (B 없으면 NULL)
```

---

## 핵심 패턴 4: 날짜 함수 ★★

```sql
-- 날짜 포맷 변환
DATE_FORMAT(col, '%Y-%m-%d')  -- 2024-03-15
DATE_FORMAT(col, '%Y%m')      -- 202403
DATE_FORMAT(col, '%H:%i')     -- 14:30

-- 날짜 부분 추출
YEAR(col)    -- 연도: 2024
MONTH(col)   -- 월: 3
DAY(col)     -- 일: 15
HOUR(col)    -- 시: 14

-- 날짜 차이 계산
DATEDIFF(날짜1, 날짜2)   -- 날짜1 - 날짜2 (일 수)
DATEDIFF('2024-03-15', '2024-03-10')  -- 5

-- 날짜 더하기/빼기
DATE_ADD(col, INTERVAL 1 DAY)    -- 1일 후
DATE_ADD(col, INTERVAL 1 MONTH)  -- 1달 후
DATE_SUB(col, INTERVAL 7 DAY)    -- 7일 전

-- 현재 날짜/시간
NOW()          -- 현재 날짜+시간
CURDATE()      -- 현재 날짜만
```

---

## 핵심 패턴 5: 문자열 함수 ★★

```sql
-- 부분 문자열
SUBSTRING(col, 시작위치, 길이)  -- 1-indexed
SUBSTRING('Hello', 2, 3)       -- 'ell'
LEFT(col, 3)                    -- 왼쪽 3글자
RIGHT(col, 3)                   -- 오른쪽 3글자

-- 패턴 매칭
WHERE col LIKE 'A%'    -- A로 시작
WHERE col LIKE '%A'    -- A로 끝
WHERE col LIKE '%A%'   -- A 포함

-- 문자열 연결
CONCAT(col1, ' ', col2)         -- "홍 길동"
CONCAT_WS('-', col1, col2)      -- "홍-길동" (구분자 포함)

-- 치환
REPLACE(col, '바꿀것', '바꾼것')
REPLACE('Hello World', 'World', 'MySQL')  -- 'Hello MySQL'

-- 문자열 길이
LENGTH(col)        -- 바이트 단위 (한글 3바이트)
CHAR_LENGTH(col)   -- 글자 수 (한글 1글자)

-- 대소문자
UPPER(col)   -- 대문자
LOWER(col)   -- 소문자
```

---

## 핵심 패턴 6: LIMIT / OFFSET ★

```sql
-- 상위 3개만
SELECT * FROM EMPLOYEES ORDER BY SALARY DESC LIMIT 3;

-- 4번째부터 6번째까지 (페이지네이션)
SELECT * FROM EMPLOYEES ORDER BY SALARY DESC LIMIT 3 OFFSET 3;
-- OFFSET: 건너뛸 행 수

-- 주의: LIMIT는 ORDER BY 뒤에 항상 마지막에
```

---

## 핵심 패턴 7: CASE WHEN ★★

```sql
-- 조건에 따라 다른 값 반환 (Python의 if-elif-else)
SELECT
    NAME,
    SALARY,
    CASE
        WHEN SALARY >= 5000 THEN '고액'
        WHEN SALARY >= 3000 THEN '중액'
        ELSE '저액'
    END AS SALARY_GRADE
FROM EMPLOYEES;

-- GROUP BY와 함께 사용
SELECT
    CASE WHEN AGE >= 30 THEN '30대 이상' ELSE '30대 미만' END AS AGE_GROUP,
    COUNT(*) AS CNT
FROM EMPLOYEES
GROUP BY AGE_GROUP;
```

---

## 핵심 패턴 8: 서브쿼리

```sql
-- 평균보다 높은 급여
SELECT NAME, SALARY
FROM EMPLOYEES
WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEES);

-- 각 지점 최고 급여자
SELECT NAME, SALARY, BRANCH_ID
FROM EMPLOYEES
WHERE (BRANCH_ID, SALARY) IN (
    SELECT BRANCH_ID, MAX(SALARY)
    FROM EMPLOYEES
    GROUP BY BRANCH_ID
);
```

---

## 핵심 패턴 9: NULL 처리

```sql
WHERE col IS NULL
WHERE col IS NOT NULL

IFNULL(col, 0)          -- NULL이면 0
COALESCE(col1, col2, 0) -- 첫 번째 NULL 아닌 값
```

---

## 핵심 패턴 10: 윈도우 함수 (순위)

```sql
RANK()       OVER (ORDER BY SALARY DESC)  -- 1,1,3 (건너뜀)
DENSE_RANK() OVER (ORDER BY SALARY DESC)  -- 1,1,2 (안 건너뜀)
ROW_NUMBER() OVER (ORDER BY SALARY DESC)  -- 1,2,3 (항상 다름)

-- 지점별 순위
RANK() OVER (PARTITION BY BRANCH_ID ORDER BY SALARY DESC)
```

---

## 자주 실수하는 것들

```sql
-- 1. ORDER BY 방향 실수
ORDER BY SALARY DESC  -- 내림차순 (높은 것부터)  ← 자주 헷갈림

-- 2. GROUP BY에 SELECT 컬럼 빠뜨리기
SELECT BRANCH_ID, NAME, SUM(SALARY)
GROUP BY BRANCH_ID, NAME  -- NAME도 GROUP BY에 넣어야 함

-- 3. HAVING에 집계함수 vs WHERE에 집계함수 오류
-- HAVING에만 집계함수(SUM, COUNT 등) 쓸 수 있음
HAVING SUM(SALARY) > 1000  -- O
WHERE SUM(SALARY) > 1000   -- X (오류)

-- 4. 컬럼명/별칭 대소문자
-- 문제에서 요구하는 컬럼명 그대로 써야 함 (대소문자 확인!)
```

---

## 프로그래머스 SQL 고득점 Kit 추천 순서

| 파트 | 우선순위 | 추천 문제 |
|------|---------|----------|
| SELECT | ★ | 여러 기준으로 정렬하기, 조건에 맞는 도서 리스트 |
| GROUP BY | ★★★ | 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기 |
| IS NULL | ★★ | 이름이 없는 동물의 아이디, 경기도에 위치한 식품창고 목록 출력 |
| JOIN | ★★★ | 없어진 기록 찾기, 있었는데요 없었습니다 |
| String/Date | ★★ | 자동차 대여 기록에서 대여중/대여 가능 여부 구분하기 |

---

## 당일 체크리스트

```
제출 전 반드시 확인:
[ ] 컬럼명/별칭 문제 요구사항과 일치하는가?
[ ] ORDER BY 방향 (ASC/DESC) 맞는가?
[ ] GROUP BY에 SELECT 컬럼 모두 포함했는가?
[ ] NULL 처리 조건 있으면 넣었는가?
[ ] 테스트케이스 실행해서 결과 확인했는가?
```
