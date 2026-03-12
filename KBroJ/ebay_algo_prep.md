# 코딩테스트 알고리즘 유형별 완전 정리
> 프로그래머스 Lv.2 기준 / 이베이재팬 코딩테스트 대비

---

## 목차
1. [시험 형식 및 풀이 흐름](#1-시험-형식-및-풀이-흐름)
2. [제약 조건으로 유형 파악](#2-제약-조건으로-유형-파악)
3. [유형 1: 정렬](#유형-1-정렬)
4. [유형 2: 해시 / 딕셔너리](#유형-2-해시--딕셔너리)
5. [유형 3: 완전탐색 / 브루트포스](#유형-3-완전탐색--브루트포스)
6. [유형 4: 스택 / 큐](#유형-4-스택--큐)
7. [유형 5: BFS (너비 우선 탐색)](#유형-5-bfs-너비-우선-탐색)
8. [유형 6: DFS (깊이 우선 탐색)](#유형-6-dfs-깊이-우선-탐색)
9. [유형 7: DP (동적 프로그래밍)](#유형-7-dp-동적-프로그래밍)
10. [유형 8: 그리디](#유형-8-그리디)
11. [유형 9: 이분탐색](#유형-9-이분탐색)
12. [유형 10: 우선순위 큐 (heapq)](#유형-10-우선순위-큐-heapq)
13. [추천 연습 문제 로드맵](#추천-연습-문제-로드맵)
14. [당일 전략](#당일-전략)

---

## 1. 시험 형식 및 풀이 흐름

### 백준 vs 프로그래머스 차이
```python
# 백준 스타일
n = int(input())
print(n * 2)

# 프로그래머스 스타일 ← 이번 시험
def solution(n):
    answer = n * 2
    return answer
```
- 입력: `input()` → 함수 파라미터로 받음
- 출력: `print()` → `return`으로 반환
- 전역변수 사용 X, 함수 안에서만 처리

### 문제 풀이 순서
```
1. 파라미터 확인   → 입력 타입 (리스트? 정수? 2차원?)
2. return 확인    → 숫자? 리스트? 문자열?
3. 제약 조건 확인  → N 크기 → 어떤 알고리즘 써야 하는지 결정
4. 예제 손으로 풀기 → 로직 검증
5. 유형 분류      → 아래 체크리스트 참고
6. 구현
7. 예제 테스트 → 제출
```

---

## 2. 제약 조건으로 유형 파악

코테는 보통 1초에 약 1억 번 연산 가능.

| N 크기 | 허용 시간복잡도 | 사용 가능한 알고리즘 |
|--------|--------------|-------------------|
| N ≤ 20 | 제한 없음 | 완전탐색, 백트래킹 |
| N ≤ 1,000 | O(N²) | 이중 for문, 완전탐색 |
| N ≤ 100,000 | O(N log N) | 정렬, 이분탐색, 우선순위 큐 |
| N ≤ 1,000,000 | O(N) | 선형탐색, DP, 해시 |

### 유형 분류 체크리스트
```
□ 순서/순위가 필요해?                       → 정렬
□ 등장 횟수 세기, 특정 값 빠르게 찾기?        → 해시
□ 경우의 수가 적어서 다 해봐도 돼? (N ≤ 20)  → 완전탐색
□ 순서가 있는 처리, 괄호/우선순위?            → 스택/큐
□ 최단 거리, 레벨별 탐색, 연결 여부?          → BFS
□ 모든 경로 탐색, 조합 생성, 사이클 감지?      → DFS
□ 이전 결과를 재사용할 수 있어? (점화식)       → DP
□ 매 순간 최선 선택이 전체 최선?              → 그리디
□ 정렬된 배열에서 특정 값 위치 찾기?          → 이분탐색
□ 매번 최솟값/최댓값 꺼내야 해?              → 우선순위 큐
```

---

## 유형 1: 정렬

### 언제?
- 순서/순위를 맞춰야 할 때
- 가장 크거나 작은 값을 찾을 때
- 두 배열의 구성이 같은지 비교할 때

### 핵심 패턴
```python
arr.sort()                                  # 오름차순 (원본 변경)
arr.sort(reverse=True)                      # 내림차순
sorted_arr = sorted(arr)                    # 원본 유지

# 커스텀 기준 정렬 (lambda)
arr.sort(key=lambda x: x[1])               # 두 번째 요소 기준 오름차순
arr.sort(key=lambda x: -x[1])              # 두 번째 요소 기준 내림차순
arr.sort(key=lambda x: (x[1], x[0]))       # 첫 기준 같으면 두 번째 기준
arr.sort(key=lambda x: (-x[1], x[0]))      # 두 번째 내림차순, 동점이면 첫 번째 오름차순

# 문자열 숫자 정렬 (가장 큰 수 만들기)
# "3" + "30" = "330" vs "30" + "3" = "303" → "330"이 큼
arr.sort(key=lambda x, y: (x+y) - (y+x))  # functools.cmp_to_key 필요
```

### 예시 문제 풀이 흐름
**문제**: 이름과 점수 쌍이 주어질 때, 점수 내림차순 / 동점이면 이름 오름차순 정렬
```python
students = [["Alice", 90], ["Bob", 85], ["Charlie", 90]]

def solution(students):
    students.sort(key=lambda x: (-x[1], x[0]))
    return students
# 결과: [["Alice",90], ["Charlie",90], ["Bob",85]]
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.1 | K번째수 | 슬라이싱 + 정렬 기본 |
| Lv.2 | 가장 큰 수 | 커스텀 정렬 기준 |
| Lv.2 | H-Index | 정렬 후 조건 탐색 |

---

## 유형 2: 해시 / 딕셔너리

### 언제?
- 등장 횟수 세기
- 특정 값 O(1)으로 빠르게 찾기
- 두 배열에 공통 원소 찾기

### 핵심 패턴
```python
# 방법 1: dict 직접
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1   # 없으면 0으로 시작

# 방법 2: defaultdict (더 간결)
from collections import defaultdict
freq = defaultdict(int)
for x in arr:
    freq[x] += 1                    # KeyError 없음

# 방법 3: Counter (가장 간결)
from collections import Counter
freq = Counter(arr)
freq["a"]           # 3 (없으면 0 반환)
freq.most_common(2) # 가장 많은 2개: [("a", 3), ("b", 2)]

# 두 배열 교집합 개수
c1, c2 = Counter(arr1), Counter(arr2)
sum((c1 & c2).values())

# set으로 중복 제거 후 탐색
s = set(arr)
if x in s:   # O(1)
    ...
```

### 예시 문제 풀이 흐름
**문제**: 두 배열에서 공통으로 등장하는 원소 개수 구하기
```python
from collections import Counter

def solution(arr1, arr2):
    c1, c2 = Counter(arr1), Counter(arr2)
    return sum((c1 & c2).values())  # 교집합 합산

# solution(["apple","banana","apple"], ["banana","apple","grape"]) → 2
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.1 | 완주하지 못한 선수 | Counter 교집합 |
| Lv.2 | 전화번호 목록 | 해시로 빠른 탐색 |
| Lv.2 | 위장 | 딕셔너리 + 조합 수 계산 |
| Lv.2 | 의상 (위장) | 카테고리별 그룹핑 |

---

## 유형 3: 완전탐색 / 브루트포스

### 언제?
- N이 작아서 모든 경우를 다 해봐도 될 때 (N ≤ 20 정도)
- 모든 조합/순열을 생성해야 할 때
- 막혔을 때 부분 점수용 첫 시도로

### 핵심 패턴
```python
from itertools import combinations, permutations, product

# 조합 (순서 무관, 중복 없음)
list(combinations([1,2,3], 2))
# [(1,2), (1,3), (2,3)]

# 순열 (순서 고려)
list(permutations([1,2,3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# 중복 조합
from itertools import combinations_with_replacement
list(combinations_with_replacement([1,2,3], 2))
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]

# 소수 판별 (완전탐색에서 자주 씀)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
```

### 예시 문제 풀이 흐름
**문제**: 숫자 배열에서 2개를 골라 합이 소수인 경우의 수
```python
from itertools import combinations

def solution(nums):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    return sum(1 for a, b in combinations(nums, 2) if is_prime(a + b))
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.1 | 모의고사 | for문 완전탐색 |
| Lv.2 | 소수 찾기 | permutations + 소수 판별 |
| Lv.2 | 카펫 | 완전탐색 + 조건 검사 |
| Lv.2 | 피로도 | permutations + 시뮬레이션 |

---

## 유형 4: 스택 / 큐

### 언제?
- **스택**: 괄호 매칭, 뒤에서부터 처리, 연산자 우선순위
- **큐**: 순서대로 처리, 대기열 시뮬레이션

### 핵심 패턴
```python
# 스택 (LIFO - 마지막에 넣은 게 먼저 나옴)
stack = []
stack.append(1)   # push
stack.pop()       # pop (마지막 요소)
stack[-1]         # 스택 맨 위 확인 (꺼내지 않음)

# 큐 (FIFO - 먼저 넣은 게 먼저 나옴)
from collections import deque
queue = deque()
queue.append(1)    # enqueue (뒤에 추가)
queue.popleft()    # dequeue (앞에서 꺼냄)
```

### 예시 문제 풀이 흐름
**문제**: 괄호 문자열이 올바른지 확인
```python
def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:                    # ')'
            if not stack:        # 스택 비어있는데 ) 나오면
                return False
            stack.pop()          # ( 와 짝 맞춤
    return len(stack) == 0       # 끝까지 돌고 스택 비어있으면 True
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.2 | 올바른 괄호 | 스택 기본 |
| Lv.2 | 기능개발 | 큐 시뮬레이션 |
| Lv.2 | 프로세스 | 큐 + 우선순위 |
| Lv.2 | 다리를 지나는 트럭 | 큐 시뮬레이션 |

---

## 유형 5: BFS (너비 우선 탐색)

### 언제?
- **최단 거리/경로** 문제 (BFS는 항상 최단 거리 보장)
- 레벨(단계)별로 탐색해야 할 때
- 연결 여부, 도달 가능 여부 확인

### 개념
```
시작점에서 가까운 곳부터 탐색. 큐를 이용.

시작: (0,0)
1단계: (0,1), (1,0)        ← 시작에서 1칸 거리
2단계: (0,2), (1,1), (2,0) ← 시작에서 2칸 거리
...
목적지 처음 도달 = 최단 거리 보장
```

### 핵심 패턴
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()       # 큐 앞에서 꺼냄
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

# 2차원 격자 BFS (상하좌우 이동)
def bfs_grid(grid, start_r, start_c):
    R, C = len(grid), len(grid[0])
    queue = deque([(start_r, start_c, 0)])  # (행, 열, 거리)
    visited = [[False] * C for _ in range(R)]
    visited[start_r][start_c] = True

    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:  # 상하좌우
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
```

### 예시 문제 풀이 흐름
**문제**: 미로에서 출발점 (0,0)에서 도착점 (N-1,M-1)까지 최단 거리
```python
from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])   # (행, 열, 거리)
    visited = [[False]*C for _ in range(R)]
    visited[0][0] = True

    while queue:
        r, c, dist = queue.popleft()
        if r == R-1 and c == C-1:   # 도착
            return dist
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist+1))
    return -1
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.2 | 게임 맵 최단거리 | 2차원 BFS 기본 |
| Lv.2 | 단어 변환 | 그래프 BFS |
| Lv.3 | 네트워크 | BFS로 연결 그룹 개수 |

---

## 유형 6: DFS (깊이 우선 탐색)

### 언제?
- 모든 경로 탐색 (완전탐색의 재귀 버전)
- 조합/순열 직접 생성 (백트래킹)
- 사이클 감지, 연결 요소 찾기

### 개념
```
한 방향으로 끝까지 파고들다가, 막히면 되돌아와서 다른 방향 탐색.
재귀 함수 or 스택으로 구현.

BFS: 넓게 퍼지며 탐색 → 최단 거리
DFS: 깊게 파고들며 탐색 → 모든 경로
```

### 핵심 패턴
```python
import sys
sys.setrecursionlimit(10**6)   # 재귀 깊이 늘리기 (파일 최상단)

# 재귀 DFS
def dfs(node, visited, graph):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, visited, graph)

# 백트래킹 (선택 → 탐색 → 되돌리기)
def backtrack(path, candidates):
    if 종료조건:
        result.append(path[:])  # 현재 경로 저장
        return
    for c in candidates:
        path.append(c)          # 선택
        backtrack(path, ...)    # 탐색
        path.pop()              # 되돌리기 ← 백트래킹 핵심
```

### 예시 문제 풀이 흐름
**문제**: 숫자 배열에서 합이 target이 되는 조합 개수 (각 숫자를 더하거나 빼서)
```python
def solution(numbers, target):
    count = 0

    def dfs(idx, current):
        nonlocal count
        if idx == len(numbers):
            if current == target:
                count += 1
            return
        dfs(idx + 1, current + numbers[idx])  # 더하기
        dfs(idx + 1, current - numbers[idx])  # 빼기

    dfs(0, 0)
    return count
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.2 | 타겟 넘버 | DFS/BFS 기본 |
| Lv.2 | 네트워크 | DFS로 연결 그룹 |
| Lv.3 | 여행경로 | DFS + 경로 추적 |

---

## 유형 7: DP (동적 프로그래밍)

### 언제?
- 같은 계산이 반복될 때 (이전 결과 재사용)
- 점화식을 세울 수 있을 때: `dp[i] = dp[i-1] + ...`
- "최대/최소/경우의 수" 문제

### 개념
```
큰 문제를 작은 문제로 쪼개고, 작은 결과를 저장해두고 재사용.

피보나치 예시:
fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)   ← fib(3) 중복 계산!

DP로 저장:
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2   ← 이미 계산됨, 그냥 꺼내씀
dp[4] = 3
dp[5] = 5
```

### 핵심 패턴
```python
# 1차원 DP
dp = [0] * (N + 1)
dp[0] = 초기값
dp[1] = 초기값
for i in range(2, N + 1):
    dp[i] = dp[i-1] + dp[i-2]   # 점화식 (문제마다 다름)

# 2차원 DP (행렬 경로 등)
dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
```

### 예시 문제 풀이 흐름
**문제**: 동전 종류가 주어질 때 금액 N을 만드는 최소 동전 수
```python
def solution(coins, N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0                              # 0원은 0개

    for coin in coins:
        for i in range(coin, N + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)  # 이 코인 사용 or 안 사용

    return dp[N] if dp[N] != float('inf') else -1
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.2 | N으로 표현 | DP + set 활용 |
| Lv.3 | 정수 삼각형 | 2차원 DP |
| Lv.3 | 도둑질 | 1차원 DP (원형 배열) |
| Lv.3 | 등굣길 | 경로 개수 DP |

---

## 유형 8: 그리디

### 언제?
- 매 순간 가장 좋은 선택이 전체적으로도 최선일 때
- "최소 횟수", "최대 이익" 문제
- 정렬 후 순서대로 처리

### 개념
```
그리디 = 욕심쟁이 전략. 지금 당장 최선을 선택.

거스름돈 예시:
1260원 거슬러줄 때 → 500 → 100 → 50 → 10 순으로 최대한 큰 단위 먼저
→ 항상 최소 개수 보장

단, 그리디가 안 되는 경우도 있음 → DP 필요
```

### 핵심 패턴
```python
# 보통 정렬 후 조건에 따라 선택
arr.sort()

result = 0
for x in arr:
    if 조건 만족:
        result += 1   # 선택
    # 아니면 pass (포기)
```

### 예시 문제 풀이 흐름
**문제**: 회의실 배정 - 시작/끝 시간이 주어질 때 최대 회의 수
```python
def solution(meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))  # 끝 시간 기준 정렬

    count = 0
    end_time = 0
    for start, end in meetings:
        if start >= end_time:   # 이전 회의 끝난 후 시작 가능
            count += 1
            end_time = end
    return count
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.1 | 체육복 | 그리디 기본 |
| Lv.2 | 조이스틱 | 그리디 + 문자열 |
| Lv.2 | 큰 수 만들기 | 스택 + 그리디 |
| Lv.3 | 섬 연결하기 | 그리디 (크루스칼) |

---

## 유형 9: 이분탐색

### 언제?
- 정렬된 배열에서 특정 값 위치 찾기 → O(log N)
- "최솟값의 최댓값" / "최댓값의 최솟값" → 정답 범위에 이분탐색
- N이 커서 선형탐색(O(N))이 느릴 때

### 개념
```
1 2 3 4 5 6 7 8 9 10 에서 7 찾기

mid = 5 → 7 > 5 → 오른쪽 탐색
mid = 8 → 7 < 8 → 왼쪽 탐색
mid = 6 → 7 > 6 → 오른쪽 탐색
mid = 7 → 찾음!

O(N) 선형: 7번 비교
O(log N) 이분: 4번 비교
```

### 핵심 패턴
```python
import bisect

arr = [1, 3, 5, 7, 9]  # 반드시 정렬 상태

# bisect_left: target 이상인 첫 위치
bisect.bisect_left(arr, 5)    # 2 (arr[2] = 5)
bisect.bisect_left(arr, 4)    # 2 (4가 들어갈 위치)

# bisect_right: target 초과인 첫 위치
bisect.bisect_right(arr, 5)   # 3 (5 다음 위치)

# 직접 구현 (조건이 복잡할 때)
lo, hi = 0, max_val
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):   # 조건 만족
        answer = mid
        lo = mid + 1  # 더 큰 값 탐색 (최댓값 구할 때)
    else:
        hi = mid - 1
```

### 예시 문제 풀이 흐름
**문제**: 정렬된 배열에서 target의 개수 구하기
```python
import bisect

def solution(arr, target):
    arr.sort()
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return right - left   # target 개수
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.3 | 입국심사 | 이분탐색 + 조건 설계 |
| Lv.3 | 징검다리 | 이분탐색 응용 |

---

## 유형 10: 우선순위 큐 (heapq)

### 언제?
- 매번 최솟값(or 최댓값)을 꺼내야 할 때
- 정렬된 상태를 유지하며 삽입/삭제 반복
- 다익스트라(최단 경로) 알고리즘

### 핵심 패턴
```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappop(heap)      # 1 (최솟값)

heap[0]                   # 현재 최솟값 확인 (꺼내지 않음)

# 최대 힙: 음수로 넣기
heapq.heappush(heap, -5)
-heapq.heappop(heap)      # 5

# (우선순위, 값) 튜플로 넣기 → 우선순위 기준 정렬
heapq.heappush(heap, (3, "task_c"))
heapq.heappush(heap, (1, "task_a"))
heapq.heappop(heap)       # (1, "task_a") 먼저 나옴
```

### 예시 문제 풀이 흐름
**문제**: 배열에서 K번째로 작은 수 구하기
```python
import heapq

def solution(arr, k):
    heapq.heapify(arr)         # 배열을 힙으로 변환
    for _ in range(k - 1):
        heapq.heappop(arr)     # k-1번 꺼내버림
    return heapq.heappop(arr)  # k번째 최솟값
```

### 추천 연습 문제
| 레벨 | 문제명 | 포인트 |
|------|--------|--------|
| Lv.2 | 디스크 컨트롤러 | 힙으로 작업 스케줄링 |
| Lv.3 | 이중우선순위큐 | 최솟값/최댓값 동시 관리 |

---

## 추천 연습 문제 로드맵

### 1단계: 기초 다지기 (Lv.1~2 쉬운 것)
| 순서 | 문제명 | 유형 | 이유 |
|------|--------|------|------|
| 1 | 완주하지 못한 선수 | 해시 | Counter 기본 |
| 2 | K번째수 | 정렬 | 슬라이싱 + sort |
| 3 | 체육복 | 그리디 | 그리디 입문 |
| 4 | 모의고사 | 완전탐색 | for문 탐색 |
| 5 | 올바른 괄호 | 스택 | 스택 기본 |
| 6 | 타겟 넘버 | DFS/BFS | DFS 입문 |

### 2단계: 핵심 유형 (Lv.2 중간)
| 순서 | 문제명 | 유형 | 이유 |
|------|--------|------|------|
| 7 | 전화번호 목록 | 해시 | 해시 탐색 |
| 8 | 위장 | 해시 | 그룹 조합 수 |
| 9 | 가장 큰 수 | 정렬 | 커스텀 정렬 |
| 10 | 소수 찾기 | 완전탐색 | permutations |
| 11 | 기능개발 | 스택/큐 | 큐 시뮬레이션 |
| 12 | 게임 맵 최단거리 | BFS | 2차원 BFS |
| 13 | 네트워크 | DFS/BFS | 연결 그룹 |
| 14 | N으로 표현 | DP | DP 입문 |
| 15 | 디스크 컨트롤러 | 힙 | heapq 실전 |

### 3단계: 심화 (Lv.2 어려운 것 ~ Lv.3)
| 순서 | 문제명 | 유형 | 이유 |
|------|--------|------|------|
| 16 | 단어 변환 | BFS | 그래프 BFS |
| 17 | 여행경로 | DFS | DFS + 경로 추적 |
| 18 | 정수 삼각형 | DP | 2차원 DP |
| 19 | 입국심사 | 이분탐색 | 이분탐색 실전 |
| 20 | 큰 수 만들기 | 그리디 | 스택 + 그리디 |

---

## 당일 전략

- **시간 배분**: 60분 / 못 풀면 50분에 부분 풀이 제출
- **부분 점수**: 테스트케이스 일부 통과도 점수 나옴
- **막히면**: 완전탐색이라도 먼저 구현해서 일부 통과시키기
- **유형 판단 순서**: 제약 조건 확인 → 체크리스트 → 구현
- **제출 전**: 예제 입출력 반드시 손으로 확인
