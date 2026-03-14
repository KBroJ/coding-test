# 알고리즘 유형별 강의
> 프로그래머스 기준 / Python3 / 빈출 순위 순

---

## 문제 보자마자 유형 찾는 법

```
① 제약 조건 확인 (N 크기)
   N ≤ 20        → 완전탐색/DFS 백트래킹
   N ≤ 1,000     → O(N²) 이중 for
   N ≤ 100,000   → O(N log N) 정렬/이분탐색
   N ≤ 1,000,000 → O(N) 해시/DP

② 키워드 확인
   "모든 경우"    → DFS
   "최단 거리"    → BFS
   "빠르게 찾기"  → 해시
   "최솟값 최댓값 반복" → heapq
   "이전 결과 재사용" → DP
   "매 순간 최선"  → 그리디
   "조건 그대로 구현" → 구현/시뮬레이션
```

---

## 기업별 출제 경향

| 기업 | 특징 | 주요 유형 |
|------|------|---------|
| **카카오** | 구현·문자열이 전반부, BFS/DFS가 후반부. 정확한 구현력 강조 | 구현, BFS/DFS, 그리디 |
| **네이버** | 2024년부터 CS 객관식 20문제 추가 | 정렬, 해시, DFS/BFS, DP |
| **라인** | 정확한 예외처리를 잘 하는지 평가 | 구현, 문자열, 완전탐색 |
| **쿠팡** | 대규모 데이터 처리 중심 | 해시, 정렬, DP |

---
---

## 유형 1: 구현 / 시뮬레이션 ★★★ (카카오 최빈출)

### 📌 한 줄 요약
> "문제에서 시킨 대로 그냥 코드로 옮기면 되는 유형"

### 🎯 언제 쓰나?
```
✓ "~한 규칙으로 이동한다"
✓ "~한 조건이면 ~를 한다"
✓ 특별한 알고리즘 없이 조건을 그대로 따라가면 되는 경우
✓ 격자(2D 배열)에서 이동, 회전, 시뮬레이션
```

### 💡 개념: 레시피 따라 요리하기

```
레시피(문제)를 보고 순서대로 실행하면 됩니다.

"감자를 3cm로 썰어라" → 조건 그대로 코드로
"물이 끓으면 라면 넣어라" → if문으로

특별한 알고리즘이 필요 없고,
문제를 꼼꼼히 읽고 정확하게 구현하는 것이 핵심.
```

### 🌳 예시: 크레인 인형뽑기

```
격자에서 인형을 뽑아 바구니에 쌓고,
같은 인형이 연속으로 2개 쌓이면 터뜨리기

[0,0,0,0,0]    바구니(스택): []
[0,0,1,0,3]
[0,2,5,0,1]    1번 열 뽑기 → 바구니: [2]
[4,2,4,4,2]    2번 열 뽑기 → 바구니: [2, 2] → 터뜨리기! → []
[3,5,1,3,1]
```

핵심 패턴: **격자 탐색 + 스택으로 터뜨리기**

### ⚙️ 코드 구조 (빈칸 채우기)

```python
def solution(board, moves):
    result = 0
    stack = []

    for col in moves:
        for row in range(len(board)):
            if board[row][col-1] != 0:
                doll = board[row][col-1]
                board[row][col-1] = ___________  # 뽑았으니 빈칸으로

                if stack and stack[-1] == ___________:  # 같은 인형이면
                    stack.pop()
                    result += ___________  # 2개 터짐
                else:
                    stack.append(___________)
                break  # 한 번만 뽑기
    return result
```

### ✅ 핵심 패턴 정리

```python
# 방향 이동 (상하좌우)
for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr, nc = r+dr, c+dc
    if 0<=nr<R and 0<=nc<C:  # 범위 체크
        ...

# 2차원 배열 초기화 (주의: [[0]*C]*R 쓰면 얕은 복사 버그!)
board = [[0]*C for _ in range(R)]
```

### 📚 추천 문제
- 크레인 인형뽑기 게임 (Lv.1)
- 문자열 압축 (Lv.2)
- 자물쇠와 열쇠 (Lv.3)

---

## 유형 2: BFS (너비 우선 탐색) ★★★

### 📌 한 줄 요약
> "가까운 곳부터 퍼져나가며 탐색 → 최단 거리 보장"

### 🎯 언제 쓰나?
```
✓ "최단 거리/경로를 구하라"
✓ "몇 번 만에 도달할 수 있나"
✓ "연결되어 있는가?"
→ BFS는 항상 최단 거리를 보장
```

### 💡 개념: 물이 퍼지는 것처럼

```
시작점에서 거리 1인 곳을 모두 탐색
→ 거리 2인 곳을 모두 탐색
→ 거리 3인 곳을 모두 탐색
→ 목적지 처음 도달 = 그게 최단 거리

🌊🌊🌊🌊🌊
🌊🌊🌊🌊🌊
🌊🌊S🌊🌊  S에서 물이 퍼짐
🌊🌊🌊🌊🌊
🌊🌊🌊🌊🌊
```

vs DFS는 "한 방향으로 끝까지 파고들기" → 최단 거리 보장 안 됨

### 🌳 예시: 미로 최단 거리

```
[1,0,1,1,1]
[1,0,1,0,1]
[1,1,1,0,1]   (0,0)에서 (2,4)까지 최단 거리?
[0,0,0,0,1]
[1,1,1,1,1]

BFS 탐색:
거리1: (1,0)
거리2: (2,0)
거리3: (2,1), (2,2)
거리4: (2,2)...
→ 목적지 처음 도달하는 거리가 답!
```

### ⚙️ 코드 구조 (빈칸 채우기)

```python
from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])       # (행, 열, 거리)
    visited = [[False]*C for _ in range(R)]
    visited[0][0] = ___________      # 시작점 방문 처리

    while queue:
        r, c, dist = queue.___________()   # 앞에서 꺼내기

        if r == ___________ and c == ___________:  # 도착 조건
            return dist

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and maps[nr][nc]==1:
                visited[nr][nc] = ___________
                queue.append((nr, nc, ___________))  # 거리 +1

    return -1   # 도달 불가
```

**질문**: `queue.pop()` 대신 `queue.popleft()`를 써야 하는 이유가 뭘까요?

### ✅ 핵심 패턴 정리

```python
from collections import deque

# 그래프 BFS (연결 여부)
def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
```

**기억법**: BFS = **B**ig **Q**ueue (deque 사용!)

### 📚 추천 문제
- 게임 맵 최단거리 (Lv.2) ← 지금 풀기 좋은 것
- 네트워크 (Lv.3)
- 단어 변환 (Lv.3)

---

## 유형 3: DFS (깊이 우선 탐색) ★★★

### 📌 한 줄 요약
> "한 방향으로 끝까지 파고들다가, 막히면 되돌아와서 모든 경우 탐색"

### 🎯 언제 쓰나?
```
✓ "모든 경우의 수를 구하라"
✓ "가능한 조합을 모두 탐색해라"
✓ "경로의 개수를 구하라"
→ BFS와 달리 최단 거리 보장 안 됨, 대신 모든 경로 탐색
```

### 💡 개념: 미로에서 왼손 법칙

```
왼쪽 벽에 손을 대고 계속 걷기
→ 막히면 되돌아와서 다른 길 선택
→ 모든 경로를 결국 다 탐색하게 됨

재귀 함수가 자연스럽게 이 구조를 만들어 줌
```

### 🌳 예시: 타겟 넘버 [1, 1, 1]

```
              시작(합=0)
             /           \
          +1(합=1)       -1(합=-1)
          /    \          /     \
       +1(2)  -1(0)    +1(0)  -1(-2)
       / \    / \      / \     / \
     +1 -1  +1 -1   +1 -1  +1  -1
     (3)(1) (1)(-1) (1)(-1)(-1)(-3)

target=1이면? → (1), (1), (1), (-1) 총 3개
```

DFS는 이 트리를 **왼쪽 끝까지 파고들었다가** 하나씩 되돌아오며 탐색

### ⚙️ 코드 구조 (빈칸 채우기)

```python
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘리기 (필수!)

def solution(numbers, target):
    count = 0

    def dfs(idx, current):
        nonlocal count

        # 종료 조건: 모든 숫자를 다 사용했을 때
        if idx == ___________:
            if current == ___________:
                count += 1
            return

        # 현재 숫자를 더하는 경우
        dfs(___________, current + numbers[idx])

        # 현재 숫자를 빼는 경우
        dfs(___________, current - numbers[idx])

    dfs(0, 0)
    return count
```

**질문 3개**:
1. `idx`는 뭘 의미하나요?
2. `nonlocal count`는 왜 필요한가요? (Java에서 없는 개념)
3. 종료 조건이 `idx == len(numbers)`인 이유는?

### ✅ 핵심 패턴 정리

```python
# 백트래킹 패턴 (선택 → 탐색 → 되돌리기)
result = []
def backtrack(path, start):
    if 종료조건:
        result.append(path[:])  # 복사해서 저장!
        return
    for i in range(start, len(candidates)):
        path.append(candidates[i])   # 선택
        backtrack(path, i+1)         # 탐색
        path.pop()                   # 되돌리기 ← 백트래킹 핵심
```

**BFS vs DFS 선택 기준**:
```
최단 거리가 필요해? → BFS
모든 경우를 탐색해야 해? → DFS
```

### 📚 추천 문제
- 타겟 넘버 (Lv.2) ← 지금 풀고 있는 것
- 네트워크 (Lv.3)
- 여행경로 (Lv.3)

---

## 유형 4: DP (동적 프로그래밍) ★★★

### 📌 한 줄 요약
> "이전에 계산한 결과를 저장해두고 재사용 → 중복 계산 제거"

### 🎯 언제 쓰나?
```
✓ "최대/최소 값을 구하라"
✓ "경우의 수를 구하라"
✓ 같은 계산이 반복될 때
✓ 점화식을 세울 수 있을 때: dp[i] = dp[i-1] + ...
```

### 💡 개념: 메모장에 적어두기

```
피보나치를 재귀로 구하면?
fib(5) → fib(4) + fib(3)
              ↓
fib(4) → fib(3) + fib(2)  ← fib(3) 중복!
fib(3) → fib(2) + fib(1)  ← fib(2) 중복!
...

계산할 때마다 메모장에 적어두면:
dp[0]=0, dp[1]=1
dp[2]=1, dp[3]=2, dp[4]=3, dp[5]=5
→ 이미 계산한 건 메모장에서 바로 꺼내 씀 (O(N))
```

### 🌳 예시: dp 테이블 채우기

```
문제: 계단 오르기 - 연속 3칸을 밟으면 안 됨, 최대 점수는?
점수: [10, 20, 15, 25, 10, 20]

dp[i] = i번째 계단까지 최대 점수

dp[1] = 10
dp[2] = 30       (1,2 같이 밟기)
dp[3] = max(
    dp[1] + 15,  → 1,3 밟기 = 25
    dp[2] + 15 는 1,2,3 연속이라 불가
    ...
)
→ 점화식을 찾는 것이 핵심!
```

### ⚙️ 코드 구조 (빈칸 채우기)

```python
# 가장 기본: 피보나치 DP
def fib(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[0] = ___________
    dp[1] = ___________
    for i in range(2, n + 1):
        dp[i] = dp[___________] + dp[___________]  # 점화식
    return dp[n]

# 동전 문제 패턴 (최소 동전 개수로 target 만들기)
def min_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = ___________   # 0원은 동전 0개
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - ___________] + 1)
    return dp[target]
```

### ✅ 핵심 패턴 정리

```python
# 1차원 DP
dp = [0] * (N + 1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]   # 문제마다 점화식 다름

# 2차원 DP (경로 문제)
dp = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
```

**핵심**: 점화식을 세우는 것이 전부. `dp[i]`가 무엇을 의미하는지 정의하고 시작.

### 📚 추천 문제
- N으로 표현 (Lv.3)
- 정수 삼각형 (Lv.3)
- 도둑질 (Lv.4)

---

## 유형 5: 해시 ★★

### 📌 한 줄 요약
> "등장 횟수 세기, 특정 값 O(1)으로 빠르게 찾기"

### 🎯 언제 쓰나?
```
✓ "등장 횟수를 구하라"
✓ "특정 값이 있는지 빠르게 확인해라"
✓ 이중 for로 O(N²) 나오는 걸 O(N)으로 줄이고 싶을 때
```

### 💡 개념: 사물함 번호표

```
이름으로 사물함 찾기:
- 일반 방법: 처음부터 하나씩 확인 → O(N)
- 해시 방법: 이름을 번호로 변환 → 번호 사물함 바로 접근 → O(1)

Python dict = Java HashMap
```

### 🌳 예시: 완주하지 못한 선수

```
참가자: ["marina", "josipa", "nikola", "vinko", "filipa"]
완주자: ["josipa", "filipa", "marina", "nikola"]

방법 1 (O(N²)): 완주자 리스트에서 한 명씩 찾기 → 느림
방법 2 (O(N)): Counter로 빈도 계산 후 비교

Counter(참가자) = {marina:1, josipa:1, nikola:1, vinko:1, filipa:1}
Counter(완주자) = {josipa:1, filipa:1, marina:1, nikola:1}
차이 = {vinko:1}  → "vinko"가 완주 못함
```

### ⚙️ 코드 구조 (빈칸 채우기)

```python
from collections import Counter

def solution(participant, completion):
    c1 = Counter(___________)   # 참가자 빈도
    c2 = Counter(___________)   # 완주자 빈도

    diff = c1 - ___________     # 차집합

    return list(diff.keys())[0]

# 또는 dict.get() 방식
def solution(participant, completion):
    d = {}
    for p in participant:
        d[p] = d.get(p, ___________) + 1   # 없으면 0으로 시작

    for c in completion:
        d[c] -= ___________

    for name, count in d.items():
        if count > 0:
            return name
```

### ✅ 핵심 패턴 정리

```python
from collections import Counter, defaultdict

# Counter: 빈도 세기
freq = Counter(arr)
freq["x"]             # 없으면 0 반환 (KeyError 없음!)
freq.most_common(2)   # 가장 많은 2개

# 교집합 개수
sum((Counter(arr1) & Counter(arr2)).values())

# defaultdict: 기본값 있는 dict
d = defaultdict(int)   # 없는 키 접근하면 자동으로 0
d["key"] += 1

# Java getOrDefault() = Python dict.get(key, default)
d.get("key", 0)
```

### 📚 추천 문제
- 완주하지 못한 선수 (Lv.1) ← 지금 풀기 좋은 것
- 전화번호 목록 (Lv.2)
- 위장 (Lv.2)
- 베스트앨범 (Lv.3)

---

## 유형 6: 그리디 ★★

### 📌 한 줄 요약
> "매 순간 최선의 선택 = 전체 최선. 단, 항상 성립하진 않음"

### 🎯 언제 쓰나?
```
✓ "최소 횟수로 ~를 해라"
✓ "최대 이익을 구하라"
✓ 정렬 후 순서대로 선택하면 되는 경우
주의: 그리디가 성립하는지 직관적으로 검증 필요
```

### 💡 개념: 거스름돈 문제

```
1260원 거스름돈 줄 때 동전 최소 개수?

욕심쟁이 전략: 큰 단위부터 최대한 사용
500원 × 2 = 1000원  → 남은 260원
100원 × 2 = 200원   → 남은 60원
50원  × 1 = 50원    → 남은 10원
10원  × 1 = 10원    → 끝

총 6개 → 최솟값!

항상 큰 단위부터 선택하는 것이 전체 최선인 이유?
→ 500원 = 100원 5개이므로, 500원을 안 쓸 이유가 없음
```

### 🌳 예시: 회의실 배정

```
[시작, 끝] = [1,4], [3,5], [0,6], [5,7], [3,9], [5,9], [6,10], [8,11]

전략: 끝나는 시간 빠른 순서로 선택
→ [1,4] 선택 (끝=4)
→ [3,5] → 시작(3) < 끝(4) → 패스
→ [5,7] 선택 (시작(5) >= 끝(4))
→ [8,11] 선택 (시작(8) >= 끝(7))
→ 총 3개!

왜 끝나는 시간 기준으로 정렬?
→ 일찍 끝날수록 다음 회의를 더 많이 잡을 수 있음
```

### ⚙️ 코드 구조 (빈칸 채우기)

```python
def solution(meetings):
    # 끝 시간 기준 정렬 (끝이 같으면 시작 기준)
    meetings.sort(key=lambda x: (___________, ___________))

    count = 0
    end_time = 0

    for start, end in meetings:
        if start >= ___________:   # 이전 회의가 끝난 후 시작 가능
            count += 1
            end_time = ___________

    return count
```

### ✅ 핵심 패턴 정리

```python
# 기본 구조: 정렬 후 조건에 따라 선택
arr.sort()

result = 0
for x in arr:
    if 조건 만족:
        result += 1   # 선택
    # 아니면 패스
```

**주의**: 그리디는 "매 순간 최선 = 전체 최선"이 성립할 때만 가능. 성립 안 하면 DP 필요.

### 📚 추천 문제
- 체육복 (Lv.1)
- 조이스틱 (Lv.2)
- 큰 수 만들기 (Lv.2)
- 구명보트 (Lv.2)

---

## 유형 7: 완전탐색 ★★

### 📌 한 줄 요약
> "N이 작을 때 모든 경우를 다 시도해보기"

### 🎯 언제 쓰나?
```
✓ N ≤ 20 정도로 작을 때
✓ 모든 조합/순열을 시도해야 할 때
✓ 막혔을 때 부분 점수용 첫 시도로
```

### 💡 개념: 자물쇠 비밀번호 찾기

```
4자리 숫자 비밀번호를 모를 때?
→ 0000부터 9999까지 다 시도 = 완전탐색

코테에서: N이 20 이하면 모든 경우 수가 2^20 = 약 100만 → 가능
N이 30이면? 2^30 = 약 10억 → 시간 초과
```

### 🌳 예시: 소수 찾기

```
숫자 카드 [1, 1, 7]로 만들 수 있는 소수의 개수

가능한 숫자들 (순열):
1자리: 1, 1, 7
2자리: 11, 17, 11, 71, 71, 17
3자리: 117, 171, 711, ...

→ 중복 제거 후 소수 판별
```

### ⚙️ 코드 구조 (빈칸 채우기)

```python
from itertools import permutations

def solution(numbers):
    nums = list(numbers)   # "011" → ['0','1','1']
    candidates = set()

    for length in range(1, len(nums)+1):
        for perm in permutations(nums, ___________):
            num = int("".join(perm))
            candidates.add(___________)   # set으로 중복 제거

    return sum(1 for n in candidates if ___________(n))   # 소수 판별

def is_prime(n):
    if n < 2: return ___________
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return ___________
    return True
```

### ✅ 핵심 패턴 정리

```python
from itertools import combinations, permutations

# 조합 (순서 무관, 중복 없음): nCr
list(combinations([1,2,3], 2))   # [(1,2),(1,3),(2,3)]

# 순열 (순서 고려): nPr
list(permutations([1,2,3], 2))   # [(1,2),(1,3),(2,1)...] 6개

# 소수 판별
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 📚 추천 문제
- 모의고사 (Lv.1)
- 소수 찾기 (Lv.2)
- 카펫 (Lv.2)
- 피로도 (Lv.2)

---

## 유형 8: 스택 / 큐 ★★

### 📌 한 줄 요약
> "스택: 마지막이 먼저 (LIFO) / 큐: 먼저 온 게 먼저 (FIFO)"

### 🎯 언제 쓰나?
```
스택 → 괄호 매칭, 뒤에서부터 처리, 연산자 우선순위, DFS
큐   → 순서대로 처리, 대기열 시뮬레이션, BFS
```

### 💡 개념: 식판 vs 줄서기

```
스택 = 식판 쌓기        큐 = 줄 서기
  [5]  ← top              [입구] 1-2-3-4 [출구]
  [4]                      먼저 온 1번이 먼저 나감
  [3]
  [2]
  [1]  ← bottom
마지막에 올린 5번이 먼저 내려감
```

### 🌳 예시: 괄호 유효성 검사

```
"(()())" → 유효한가?

스택으로 처리:
( → 스택: [(]
( → 스택: [(, (]
) → 짝 맞춤 → 스택: [(]
( → 스택: [(, (]
) → 짝 맞춤 → 스택: [(]
) → 짝 맞춤 → 스택: []
끝났을 때 스택 비어있음 → 유효!

"(()" → 스택: [(] 남음 → 유효하지 않음!
```

### ⚙️ 코드 구조 (빈칸 채우기)

```python
# 괄호 검사
def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:   # ')'
            if not ___________:   # 스택이 비어있으면
                return False
            stack.___________()   # ( 꺼내기

    return len(stack) == ___________  # 끝까지 돌고 비어있으면 True

# 큐 시뮬레이션
from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))  # (인덱스, 우선순위)
    order = 0

    while queue:
        idx, priority = queue.popleft()

        if any(priority < p for _, p in queue):  # 뒤에 더 높은 우선순위 있으면
            queue.append((idx, priority))         # 맨 뒤로
        else:
            order += ___________
            if idx == ___________:
                return order
```

### ✅ 핵심 패턴 정리

```python
from collections import deque

# 스택 (list 사용)
stack = []
stack.append(x)   # push O(1)
stack.pop()       # pop O(1)
stack[-1]         # top 확인

# 큐 (deque 사용! list.pop(0)은 O(N)이라 느림)
queue = deque()
queue.append(x)    # enqueue O(1)
queue.popleft()    # dequeue O(1) ← list.pop(0)은 O(N)이라 안 됨!
```

### 📚 추천 문제
- 올바른 괄호 (Lv.2)
- 기능개발 (Lv.2)
- 프로세스 (Lv.2)
- 다리를 지나는 트럭 (Lv.2)

---

## 유형 9: 이분탐색 / heapq ★

### 📌 한 줄 요약
> "이분탐색: 정렬된 배열에서 O(log N) 탐색 / heapq: 최솟값을 빠르게"

### 🎯 언제 쓰나?
```
이분탐색:
✓ 정렬된 배열에서 특정 값 위치 찾기
✓ "최솟값의 최댓값" / "최댓값의 최솟값" 구하기

heapq:
✓ 매번 최솟값(또는 최댓값)을 꺼내야 할 때
✓ 다익스트라 알고리즘
```

### 💡 개념

```
이분탐색 = 업다운 게임
1~100 사이 숫자 맞추기:
→ 50? "업" → 75? "다운" → 62? "업" → ...
→ O(log N)번만에 찾음 (최대 7번으로 100개 탐색)

heapq = 우선순위가 있는 줄서기
→ 번호표 뽑을 때 작은 번호가 항상 먼저 나오는 큐
```

### ⚙️ 코드 구조 (빈칸 채우기)

```python
import bisect, heapq

# 이분탐색: 정렬된 배열에서 target 개수 구하기
def count_target(arr, target):
    arr.sort()
    left = bisect.bisect_left(arr, ___________)   # target 이상인 첫 위치
    right = bisect.bisect_right(arr, ___________)  # target 초과인 첫 위치
    return right - left

# heapq: K번째 작은 수
def kth_smallest(arr, k):
    heapq.heapify(arr)
    for _ in range(k - 1):
        heapq.heappop(arr)          # k-1번 꺼내버림
    return heapq.heappop(arr)       # k번째

# 최대 힙 (음수 트릭)
heap = []
heapq.heappush(heap, ___________)  # -x로 넣기
-heapq.heappop(heap)               # 꺼낼 때 다시 음수
```

### ✅ 핵심 패턴 정리

```python
# 직접 이분탐색 (조건이 복잡할 때)
lo, hi = 0, max_val
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):       # 조건 만족
        answer = mid
        lo = mid + 1     # 더 큰 값 탐색 (최댓값 구할 때)
    else:
        hi = mid - 1
```

### 📚 추천 문제
- 더 맵게 (Lv.2) ← heapq 입문
- 디스크 컨트롤러 (Lv.3)
- 입국심사 (Lv.3) ← 이분탐색 입문
- 징검다리 (Lv.4)

---

## 단기 집중 연습 순서

| # | 문제명 | 유형 | 오늘 풀어야 하면? |
|---|--------|------|----------------|
| 1 | 타겟 넘버 | DFS | ★ 지금 진행 중 |
| 2 | 게임 맵 최단거리 | BFS | ★ 오늘 |
| 3 | 완주하지 못한 선수 | 해시 | ★ 오늘 (빠르게) |
| 4 | 네트워크 | DFS/BFS | 여유 있으면 |
| 5 | 기능개발 | 큐 시뮬레이션 | 여유 있으면 |
