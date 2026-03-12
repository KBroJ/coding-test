# Python 치트시트 (시험장용)
> 프로그래머스 전용 / 핵심만 압축

---

## 프로그래머스 필수: 함수 형태

```python
# 반드시 이 형태! input()/print() 절대 사용 X
def solution(param1, param2):
    answer = ...
    return answer

# 파라미터 타입 확인 먼저
# int, str, list, list of list → 각각 처리 방식 다름
```

---

## 자주 쓰는 import

```python
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product
import heapq
import sys
sys.setrecursionlimit(10**6)  # DFS 재귀 쓸 때 맨 위에
```

---

## 정렬

```python
arr.sort()                              # 오름차순 (원본 변경)
arr.sort(reverse=True)                  # 내림차순
sorted_arr = sorted(arr)                # 원본 유지
arr.sort(key=lambda x: x[1])           # 두 번째 요소 기준
arr.sort(key=lambda x: (-x[1], x[0])) # 두 번째 내림, 첫 번째 오름
```

---

## 리스트 컴프리헨션

```python
[x*2 for x in arr]                    # 기본
[x for x in arr if x > 0]            # 조건 필터
[x*y for x in a for y in b]          # 이중 for

# 2차원 리스트 생성
matrix = [[0]*C for _ in range(R)]    # R행 C열 0으로 초기화
# 주의: [[0]*C]*R 는 얕은 복사라 안 됨!
```

---

## Counter (빈도 세기)

```python
from collections import Counter

freq = Counter(arr)
freq["a"]            # 3 (없으면 0 반환, KeyError 없음)
freq.most_common(2)  # [("a",3), ("b",2)] 가장 많은 2개

# 교집합 (공통 원소 개수)
c1, c2 = Counter(arr1), Counter(arr2)
sum((c1 & c2).values())
```

---

## defaultdict

```python
from collections import defaultdict

d = defaultdict(int)   # 기본값 0
d["key"] += 1          # KeyError 없음

d = defaultdict(list)  # 기본값 []
d["key"].append(1)

# 일반 dict.get() 쓸 때
d.get("key", 0)        # Java의 getOrDefault()
```

---

## deque (큐/양방향 큐)

```python
from collections import deque

q = deque()
q.append(x)      # 뒤에 추가
q.popleft()      # 앞에서 꺼냄 (O(1), list.pop(0)은 O(N))
q.appendleft(x)  # 앞에 추가
q.pop()          # 뒤에서 꺼냄

# 초기화
q = deque([1, 2, 3])
```

---

## heapq (우선순위 큐)

```python
import heapq

heap = []
heapq.heappush(heap, 5)    # 삽입
heapq.heappop(heap)        # 최솟값 꺼냄
heap[0]                    # 최솟값 확인 (꺼내지 않음)

# 최대 힙: 음수로 넣기
heapq.heappush(heap, -5)
-heapq.heappop(heap)       # 5

# 리스트를 힙으로
heapq.heapify(arr)         # 제자리에서 O(N)

# (우선순위, 값) 패턴
heapq.heappush(heap, (1, "high"))
heapq.heappush(heap, (3, "low"))
heapq.heappop(heap)        # (1, "high")
```

---

## BFS 템플릿 (외워두기)

```python
from collections import deque

# 그래프 BFS
def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

# 2차원 격자 BFS (최단 거리)
def bfs_grid(grid, sr, sc):
    R, C = len(grid), len(grid[0])
    queue = deque([(sr, sc, 0)])     # (행, 열, 거리)
    visited = [[False]*C for _ in range(R)]
    visited[sr][sc] = True
    while queue:
        r, c, dist = queue.popleft()
        if r == R-1 and c == C-1:   # 도착 조건 (예시)
            return dist
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:  # 상하좌우
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==1:
                visited[nr][nc] = True
                queue.append((nr, nc, dist+1))
    return -1
```

---

## DFS 템플릿 (외워두기)

```python
import sys
sys.setrecursionlimit(10**6)  # 맨 위에 선언

# 재귀 DFS
def dfs(node, visited, graph):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, visited, graph)

# 백트래킹 (선택 → 탐색 → 되돌리기)
result = []
def backtrack(path, start):
    if len(path) == k:           # 종료 조건 (문제마다 다름)
        result.append(path[:])   # 복사해서 저장!
        return
    for i in range(start, len(candidates)):
        path.append(candidates[i])
        backtrack(path, i+1)
        path.pop()               # 핵심: 되돌리기

# 합이 target인 경우 세기
def dfs_count(idx, current, numbers, target):
    if idx == len(numbers):
        return 1 if current == target else 0
    return (dfs_count(idx+1, current+numbers[idx], numbers, target) +
            dfs_count(idx+1, current-numbers[idx], numbers, target))
```

---

## 완전탐색

```python
from itertools import combinations, permutations

list(combinations([1,2,3], 2))   # [(1,2),(1,3),(2,3)]
list(permutations([1,2,3], 2))   # [(1,2),(1,3),(2,1),...] 6개

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

---

## 자주 쓰는 문자열 패턴

```python
# 문자열 → 리스트
list("abc")           # ['a','b','c']
"abc".split()         # ['abc'] (공백 없으면 전체)
"a,b,c".split(",")    # ['a','b','c']

# 리스트 → 문자열
"".join(['a','b','c'])    # 'abc'
",".join(['a','b','c'])   # 'a,b,c'

# 자주 쓰는 메서드
s.count("a")          # 'a' 개수
s.find("ab")          # 처음 위치 (-1 if not found)
s.startswith("ab")    # 접두사 확인
s.endswith("ab")      # 접미사 확인
s[::-1]               # 뒤집기
ord('A')              # 65 (ASCII)
chr(65)               # 'A'
```

---

## 좌표/격자 패턴

```python
# 상하좌우
for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr, nc = r+dr, c+dc

# 범위 체크
if 0<=nr<R and 0<=nc<C:

# 2차원 배열 초기화
board = [[0]*C for _ in range(R)]

# 회전 (시계방향 90도)
# (r, c) → (c, R-1-r)
```

---

## 제출 전 실수 방지 체크리스트

```
[ ] input() 사용했나? → 파라미터로 받아야 함
[ ] print() 남아있나? → return으로 반환
[ ] 디버그용 print() 삭제했나?
[ ] sys.setrecursionlimit 선언했나? (DFS 쓸 때)
[ ] 2차원 리스트 [[0]*C]*R 로 만들었나? → 얕은 복사 버그
[ ] deque 쓸 때 popleft() 썼나? (pop(0)은 O(N))
[ ] 예제 입출력 손으로 확인했나?
[ ] return 타입 맞는가? (int? list? str?)
[ ] 인덱스 범위 벗어나는 경우 있나?
[ ] 빈 배열/0 입력 엣지 케이스 처리했나?
```
