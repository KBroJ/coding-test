# 이베이재팬 코딩테스트 - SQL 준비
> MySQL / 1문제 / 권장 시간 30분

---

## 문제 풀이 흐름

```
1. 어떤 테이블이 있는지 확인
2. 뭘 출력해야 하는지 확인 (컬럼명, 별칭)
3. 조건이 뭔지 확인 (WHERE, HAVING)
4. 정렬 기준 확인 (ORDER BY)
5. 집계 필요한지 확인 (GROUP BY)
6. 테이블 여러 개면 JOIN 필요한지 확인
7. 테스트 돌려보기 → 제출
```

---

## 핵심 패턴 1: GROUP BY + 집계함수

**가장 자주 나오는 패턴!** 데모 문제도 이 유형이었어요.

```sql
-- 지점별 총 급여 합산, 지점ID 오름차순
SELECT
    BRANCH_ID,
    SUM(SALARY) AS TOTAL
FROM EMPLOYEES
GROUP BY BRANCH_ID
ORDER BY BRANCH_ID;

-- 집계함수 종류
SUM(컬럼)    -- 합계
AVG(컬럼)    -- 평균
COUNT(*)     -- 행 수
MAX(컬럼)    -- 최댓값
MIN(컬럼)    -- 최솟값
```

---

## 핵심 패턴 2: JOIN

```sql
-- INNER JOIN: 양쪽 다 있는 것만 (가장 많이 쓰임)
SELECT e.NAME, d.DEPT_NAME
FROM EMPLOYEES e
INNER JOIN DEPARTMENT d ON e.BRANCH_ID = d.ID;

-- LEFT JOIN: 왼쪽 기준, 오른쪽 없으면 NULL
SELECT e.NAME, d.DEPT_NAME
FROM EMPLOYEES e
LEFT JOIN DEPARTMENT d ON e.BRANCH_ID = d.ID;
```

**JOIN 종류 차이**
```
INNER JOIN:  A ∩ B  (양쪽 다 있는 것)
LEFT JOIN:   A 전체 (B 없으면 NULL)
RIGHT JOIN:  B 전체 (A 없으면 NULL)
```

---

## 핵심 패턴 3: WHERE vs HAVING

```sql
-- WHERE: GROUP BY 전에 필터 (개별 행 기준)
-- HAVING: GROUP BY 후에 필터 (그룹 기준)

-- 예: 급여 200 이상인 직원들 중, 지점별 합산이 500 이상인 지점
SELECT BRANCH_ID, SUM(SALARY)
FROM EMPLOYEES
WHERE SALARY >= 200          -- 먼저 개별 필터
GROUP BY BRANCH_ID
HAVING SUM(SALARY) >= 500;   -- 그룹 집계 후 필터
```

---

## 핵심 패턴 4: 서브쿼리

```sql
-- 평균보다 높은 급여를 받는 직원
SELECT NAME, SALARY
FROM EMPLOYEES
WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEES);

-- 각 지점에서 가장 높은 급여를 받는 직원
SELECT NAME, SALARY, BRANCH_ID
FROM EMPLOYEES
WHERE (BRANCH_ID, SALARY) IN (
    SELECT BRANCH_ID, MAX(SALARY)
    FROM EMPLOYEES
    GROUP BY BRANCH_ID
);
```

---

## 핵심 패턴 5: NULL 처리

```sql
-- NULL 체크
WHERE 컬럼 IS NULL
WHERE 컬럼 IS NOT NULL

-- NULL이면 다른 값으로
SELECT IFNULL(SALARY, 0) FROM EMPLOYEES;   -- MySQL
SELECT COALESCE(SALARY, 0) FROM EMPLOYEES; -- 표준 SQL
```

---

## 핵심 패턴 6: 윈도우 함수 (순위)

```sql
-- 급여 순위 (동일 급여면 같은 순위)
SELECT
    NAME,
    SALARY,
    RANK() OVER (ORDER BY SALARY DESC) AS RNK
FROM EMPLOYEES;

-- 지점별 급여 순위
SELECT
    NAME,
    SALARY,
    BRANCH_ID,
    RANK() OVER (PARTITION BY BRANCH_ID ORDER BY SALARY DESC) AS RNK
FROM EMPLOYEES;

-- 순위 함수 종류
RANK()        -- 동점이면 같은 순위, 다음 순위 건너뜀 (1,1,3)
DENSE_RANK()  -- 동점이면 같은 순위, 다음 순위 안 건너뜀 (1,1,2)
ROW_NUMBER()  -- 동점 상관없이 순서대로 (1,2,3)
```

---

## 자주 실수하는 것들

```sql
-- 1. ORDER BY 방향 반대로 하는 실수
ORDER BY SALARY DESC   -- 내림차순 (높은 것부터)
ORDER BY SALARY ASC    -- 오름차순 (낮은 것부터, 기본값)

-- 2. 조건 범위 실수 (이상/초과, 이하/미만)
>= 200   -- 200 이상 (200 포함)
> 200    -- 200 초과 (200 미포함)

-- 3. 별칭(AS) 잊기
SELECT SUM(SALARY) AS TOTAL   -- AS로 컬럼명 지정

-- 4. GROUP BY에 SELECT 컬럼 빠뜨리기
SELECT BRANCH_ID, NAME, SUM(SALARY)  -- NAME도 GROUP BY에 있어야 함
GROUP BY BRANCH_ID, NAME
```

---

## 데모 문제 풀이 분석

**문제**: EMPLOYEES 테이블에서 지점별 총 급여 합산을 지점ID 오름차순으로 출력

```sql
SELECT
    BRANCH_ID,
    SUM(SALARY) AS TOTAL
FROM
    EMPLOYEES
GROUP BY BRANCH_ID
ORDER BY BRANCH_ID;
```

**풀이 포인트**
- GROUP BY로 지점별 묶기
- SUM()으로 급여 합산
- ORDER BY로 오름차순 정렬
- AS로 컬럼명 지정 (문제에서 요구하는 컬럼명 확인!)

---

## 당일 전략

- **문제 조건 꼼꼼히 읽기**: "상위 3개", "NULL 제외" 같은 디테일 놓치면 틀림
- **테스트 먼저 돌리기**: 제출 전 반드시 테스트케이스 확인
- **컬럼명 확인**: 문제에서 요구하는 컬럼명/별칭 그대로 맞추기
- **시간 배분**: 30분 목표, 막히면 20분 안에 아는 것까지 작성 후 제출

---

## 프로그래머스 SQL 추천 연습 문제

| 파트 | 우선순위 |
|------|---------|
| SELECT | 기본기 확인 |
| GROUP BY | ★★★ 필수 |
| IS NULL | ★★ 중요 |
| JOIN | ★★★ 필수 |
| String, Date | ★ 여유 있으면 |
