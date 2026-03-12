# 알고리즘 집중 준비
> eBay Japan 코딩테스트 / Python3 / 80분 목표

---

## 유형 판단 체크리스트 (빠른 버전)

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

## 데모 문제 해설: 직사각형 + 점 포함 여부

### 문제 유형
4개의 점 좌표로 축 정렬 직사각형(bounding box) 만들고,
주어진 점이 직사각형 안에 포함되는지 확인

### 핵심 패턴: Bounding Box

```python
def solution(rectangle_points, query_points):
    # 4개 점에서 bounding box 계산
    xs = [p[0] for p in rectangle_points]
    ys = [p[1] for p in rectangle_points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    results = []
    for qx, qy in query_points:
        # 점이 직사각형 내부에 있는지 (경계 포함)
        if min_x <= qx <= max_x and min_y <= qy <= max_y:
            results.append(True)
        else:
            results.append(False)
    return results
```

### 변형: 여러 직사각형에서 점 포함 여부

```python
def point_in_rect(rect, point):
    x1, y1, x2, y2 = rect   # (왼쪽위_x, 왼쪽위_y, 오른쪽아래_x, 오른쪽아래_y)
    px, py = point
    return min(x1,x2) <= px <= max(x1,x2) and min(y1,y2) <= py <= max(y1,y2)

def solution(rectangles, points):
    return [any(point_in_rect(r, p) for r in rectangles) for p in points]
```

---

## 구현/시뮬레이션 유형

### 언제?
- 문제 조건을 그대로 코드로 옮기면 되는 유형
- 좌표 이동, 회전, 시뮬레이션

### 핵심 패턴

```python
# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 또는
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# 격자 범위 체크
def in_bounds(r, c, R, C):
    return 0 <= r < R and 0 <= c < C

# 회전 (시계방향 90도)
# (r, c) → (c, R-1-r)  [R: 행 개수]

# 2차원 배열 생성
board = [[0]*C for _ in range(R)]

# 문자열을 격자로
grid = [list(row) for row in input_list]
```

### 자주 나오는 시뮬레이션 패턴

```python
# 플레이어 이동 시뮬레이션
def solution(board, moves):
    result = 0
    hand = []   # 스택으로 손에 든 카드

    for col in moves:
        # 해당 열에서 위에서 첫 번째 인형 찾기
        for row in range(len(board)):
            if board[row][col-1] != 0:
                doll = board[row][col-1]
                board[row][col-1] = 0

                # 손에 같은 인형이 있으면 터트리기
                if hand and hand[-1] == doll:
                    hand.pop()
                    result += 2
                else:
                    hand.append(doll)
                break
    return result
```

---

## 우선순위 8문제 (3일 안에 풀 분량)

### Day 1 (3/12) - SQL/에세이 날이라 패스, 가볍게 1문제
| # | 문제명 | 유형 | 핵심 |
|---|--------|------|------|
| 1 | 완주하지 못한 선수 | 해시 | Counter 기본 |

### Day 2 (3/13) - 알고리즘 집중일, 7문제
| # | 문제명 | 유형 | 핵심 |
|---|--------|------|------|
| 2 | 기능개발 | 큐 시뮬레이션 | 조건별 처리 |
| 3 | 타겟 넘버 | DFS | 재귀 기본 |
| 4 | 게임 맵 최단거리 | BFS | 2차원 BFS |
| 5 | 소수 찾기 | 완전탐색 | permutations + is_prime |
| 6 | 카펫 | 완전탐색 | 이중 for + 조건 검사 |
| 7 | 전화번호 목록 | 해시 | startswith |
| 8 | 위장 | 해시+수학 | 딕셔너리 그룹 |

> 프로그래머스 → 코딩테스트 연습 → 해시/스택큐/DFS-BFS/완전탐색 파트

---

## 알고리즘별 핵심 코드 패턴

### 해시/딕셔너리
```python
from collections import Counter, defaultdict

# 빈도 세기
freq = Counter(arr)
freq["x"]           # 없으면 0 반환 (KeyError 없음)

# 기본값 있는 dict
d = defaultdict(int)
d["key"] += 1

# dict.get() - Java의 getOrDefault()
d.get("key", 0)
```

### BFS (외워두기)
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

# 2차원 격자 BFS
def bfs_grid(grid, sr, sc):
    R, C = len(grid), len(grid[0])
    queue = deque([(sr, sc, 0)])
    visited = [[False]*C for _ in range(R)]
    visited[sr][sc] = True
    while queue:
        r, c, d = queue.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==1:
                visited[nr][nc] = True
                queue.append((nr, nc, d+1))
```

### DFS (외워두기)
```python
import sys
sys.setrecursionlimit(10**6)

# 재귀 DFS
def dfs(node, visited, graph):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, visited, graph)

# 백트래킹
def backtrack(path):
    if 종료조건:
        result.append(path[:])
        return
    for nxt in candidates:
        path.append(nxt)
        backtrack(path)
        path.pop()   # 핵심: 되돌리기
```

### 정렬 (자주 쓰는 패턴)
```python
arr.sort()                           # 오름차순
arr.sort(reverse=True)               # 내림차순
arr.sort(key=lambda x: x[1])        # 두 번째 요소 기준
arr.sort(key=lambda x: (-x[1], x[0]))  # 두 번째 내림, 첫 번째 오름
```

### 완전탐색
```python
from itertools import combinations, permutations

list(combinations([1,2,3], 2))   # 조합 (순서 무관)
list(permutations([1,2,3], 2))   # 순열 (순서 고려)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 스택/큐
```python
from collections import deque

stack = []
stack.append(x)   # push
stack.pop()       # pop (뒤에서)
stack[-1]         # top 확인

queue = deque()
queue.append(x)   # enqueue
queue.popleft()   # dequeue (앞에서)
```

---

## 당일 전략

```
1. N 크기 보고 알고리즘 결정
2. 손으로 예제 1개 풀어보기
3. 막히면 완전탐색이라도 먼저 제출 (부분 점수)
4. 50분 지나면 미련 없이 다음 문제로
```
