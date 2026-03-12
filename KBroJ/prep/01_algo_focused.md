# 알고리즘 집중 준비
> 프로그래머스 기준 / Python3 / 빈출 유형 기반

---

## 유형 판단 체크리스트

```
N 크기 확인:
  N ≤ 20       → 완전탐색/백트래킹
  N ≤ 1,000    → O(N²) 이중 for
  N ≤ 100,000  → O(N log N) 정렬/이분탐색
  N ≤ 1,000,000 → O(N) 해시/DP/선형탐색

유형 키워드:
  최단 거리/경로     → BFS
  모든 경우 탐색     → DFS/백트래킹
  등장 횟수/빠른 탐색 → 해시(Counter/dict)
  최소/최대 반복     → heapq
  이전 결과 재사용   → DP
  매 순간 최선       → 그리디
  좌표/범위/격자     → 구현/시뮬레이션
```

---

## 기업별 출제 경향

| 기업 | 특징 | 주요 유형 |
|------|------|---------|
| **카카오** | 구현·문자열이 전반부, BFS/DFS가 후반부. 특별한 알고리즘보다 정확한 구현력 강조. 2023년부터 그리디 비중 증가 | 구현, 문자열, BFS/DFS, 그리디 |
| **네이버(팀네이버)** | 2024년부터 CS 객관식 20문제 추가. 알고리즘은 정렬·해시·BFS/DFS 위주 | 정렬, 해시, DFS/BFS, DP |
| **라인** | 복잡한 알고리즘보다 문제를 정확히 읽고 예외처리 잘 하는지 평가 | 구현, 문자열, 완전탐색 |
| **쿠팡** | 대규모 데이터 처리, 실무 연관성 높은 문제 선호 | 해시, 정렬, DP |

---

## 빈출 유형 TOP 8 (출제 빈도 순)

### 1순위: 구현 / 시뮬레이션 ★★★
문제 조건을 그대로 코드로 옮기는 능력. 카카오에서 매년 가장 많이 출제.

```python
# 방향 벡터 (상하좌우)
for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr, nc = r+dr, c+dc
    if 0<=nr<R and 0<=nc<C:
        ...

# 2차원 배열 초기화
board = [[0]*C for _ in range(R)]

# 스택 활용 시뮬레이션 (같은 것 터뜨리기)
stack = []
for x in arr:
    if stack and stack[-1] == x:
        stack.pop()
    else:
        stack.append(x)
```

**추천 문제**: 크레인 인형뽑기, 자물쇠와 열쇠, 문자열 압축, 괄호 변환

---

### 2순위: BFS / DFS ★★★
카카오 역대 기출 최빈출. BFS는 최단거리, DFS는 모든 경로.

```python
# BFS (최단거리)
from collections import deque

def bfs_grid(grid, sr, sc):
    R, C = len(grid), len(grid[0])
    queue = deque([(sr, sc, 0)])
    visited = [[False]*C for _ in range(R)]
    visited[sr][sc] = True
    while queue:
        r, c, dist = queue.popleft()
        if r == R-1 and c == C-1:
            return dist
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==1:
                visited[nr][nc] = True
                queue.append((nr, nc, dist+1))
    return -1

# DFS (타겟 넘버 패턴)
def dfs(idx, current, numbers, target):
    if idx == len(numbers):
        return 1 if current == target else 0
    return (dfs(idx+1, current+numbers[idx], numbers, target) +
            dfs(idx+1, current-numbers[idx], numbers, target))
```

**추천 문제**: 게임 맵 최단거리, 타겟 넘버, 네트워크, 단어 변환, 여행경로

---

### 3순위: DP (동적 프로그래밍) ★★★

```python
# 1차원 DP
dp = [0] * (N + 1)
dp[0], dp[1] = 0, 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

# 배낭/동전 패턴
dp = [float('inf')] * (target + 1)
dp[0] = 0
for item in items:
    for i in range(item, target+1):
        dp[i] = min(dp[i], dp[i-item] + 1)
```

**추천 문제**: N으로 표현, 도둑질, 정수 삼각형, 등굣길

---

### 4순위: 해시 ★★

```python
from collections import Counter, defaultdict

freq = Counter(arr)
freq["x"]           # 없으면 0 반환

# 교집합 개수
c1, c2 = Counter(arr1), Counter(arr2)
sum((c1 & c2).values())

d = defaultdict(int)
for x in arr:
    d[x] += 1
```

**추천 문제**: 완주하지 못한 선수, 전화번호 목록, 위장, 베스트앨범

---

### 5순위: 그리디 ★★

```python
# 보통 정렬 후 조건에 따라 선택
arr.sort(key=lambda x: x[1])  # 끝 시간 기준 정렬
result, end = 0, 0
for start, finish in arr:
    if start >= end:
        result += 1
        end = finish
```

**추천 문제**: 체육복, 큰 수 만들기, 조이스틱, 구명보트

---

### 6순위: 완전탐색 ★★

```python
from itertools import combinations, permutations

list(combinations([1,2,3], 2))   # 조합
list(permutations([1,2,3], 2))   # 순열

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

**추천 문제**: 모의고사, 소수 찾기, 카펫, 피로도

---

### 7순위: 스택 / 큐 ★★

```python
from collections import deque

stack = []
stack.append(x); stack.pop()

queue = deque()
queue.append(x); queue.popleft()  # O(1)
```

**추천 문제**: 올바른 괄호, 기능개발, 프로세스, 다리를 지나는 트럭

---

### 8순위: 이분탐색 / heapq ★

```python
import bisect, heapq

# 이분탐색
bisect.bisect_left(arr, target)

# 직접 구현 (조건이 복잡할 때)
lo, hi = 0, max_val
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid): answer = mid; lo = mid + 1
    else: hi = mid - 1

# 최소힙
heapq.heappush(heap, x); heapq.heappop(heap)
# 최대힙: 음수 트릭
heapq.heappush(heap, -x); -heapq.heappop(heap)
```

**추천 문제**: 입국심사, 징검다리, 더 맵게, 디스크 컨트롤러

---

## 구현/시뮬레이션 추가 패턴

### Bounding Box + 점 포함 여부

```python
def solution(rectangle_points, query_points):
    xs = [p[0] for p in rectangle_points]
    ys = [p[1] for p in rectangle_points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    return [min_x<=qx<=max_x and min_y<=qy<=max_y for qx,qy in query_points]
```

---

## 단기 집중 연습 문제 (우선순위 순)

| # | 문제명 | 유형 | 핵심 포인트 |
|---|--------|------|------------|
| 1 | 완주하지 못한 선수 | 해시 | Counter 기본 |
| 2 | 기능개발 | 큐 시뮬레이션 | 조건별 처리 |
| 3 | 타겟 넘버 | DFS | 재귀 DFS 기본 |
| 4 | 게임 맵 최단거리 | BFS | 2차원 BFS |
| 5 | 소수 찾기 | 완전탐색 | permutations + is_prime |
| 6 | 전화번호 목록 | 해시 | startswith 패턴 |
| 7 | 위장 | 해시+수학 | 그룹별 조합 수 |
| 8 | 네트워크 | DFS/BFS | 연결 그룹 개수 |

---

## 당일 전략

```
1. N 크기 보고 알고리즘 결정
2. 손으로 예제 1개 풀어보기
3. 막히면 완전탐색이라도 먼저 제출 (부분 점수)
4. 50분 지나면 미련 없이 다음 문제로
```
