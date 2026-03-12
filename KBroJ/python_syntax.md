# 코딩테스트 Python 문법 정리 (Java 비교)

## 목차
1. [입출력](#1-입출력)
2. [조건문](#2-조건문)
3. [반복문](#3-반복문)
4. [배열 (List)](#4-배열-list)
5. [딕셔너리 (dict)](#5-딕셔너리-dict)
6. [문자열](#6-문자열)
7. [유용한 내장 함수](#7-유용한-내장-함수)
8. [코테 필수 모듈](#8-코테-필수-모듈)

---

## 1. 입출력

### 입력
```python
n = input()                            # 문자열로 입력받음
n = int(input())                       # 정수로 입력받음
a, b, c = map(int, input().split())    # "1 2 3" → a=1, b=2, c=3
arr = list(map(int, input().split()))  # "1 2 3" → [1, 2, 3]
```

### 출력
```python
print("hello")            # hello
print(1, 2, 3)            # 1 2 3 (공백 구분)
print(1, 2, 3, sep=",")   # 1,2,3 (구분자 지정)
print("hi", end=" ")      # 줄바꿈 없이 출력
```

### 변수 포함 출력
```python
d, n, a = 3, 5, "축구"

print(f"{d}일에 {n}명과 {a}를 했다")           # f-string (추천!)
print("{}일에 {}명과 {}를 했다".format(d, n, a)) # .format()
```

### 빠른 입출력 (대용량 입력 시 필수)
```python
import sys
input = sys.stdin.readline   # input()을 빠른 버전으로 교체
print = sys.stdout.write     # print()를 빠른 버전으로 교체

# sys.stdout.write 주의사항
# - 문자열만 받음 (숫자 직접 전달 불가)
# - 줄바꿈(\n) 직접 붙여야 함
print("hello\n")              # O
print(str(123) + "\n")        # O
print(123)                    # X → TypeError!

# 배열 출력 패턴 (코테 자주 사용)
print(' '.join(map(str, arr)) + '\n')
```

### 소수점 자릿수 고정 출력
```python
v = 80.0
print(f"{v:.2f}")        # '80.00' (소수점 둘째 자리 고정 + 반올림)
print(f"${v:.2f}")       # '$80.00' (달러 기호 포함)

# round()와의 차이
round(47.992, 2)         # → 47.99  (숫자 반환, 계산에 다시 쓸 때)
round(80.0, 2)           # → 80.0   (자릿수 고정 안 됨!)
f"{80.0:.2f}"            # → '80.00' (문자열 반환, 출력할 때)
```

### f-string 포맷 옵션
```python
# 소수점
f"{3.14159:.2f}"    # '3.14'    (소수점 둘째 자리)

# 정수 자릿수 (앞에 0 채우기) - 시간/날짜 출력에 자주 사용
f"{7:02d}"          # '07'      (2자리, 0으로 채움)
f"{7:05d}"          # '00007'   (5자리, 0으로 채움)

# 정렬
f"{'hi':>10}"       # '        hi'  (오른쪽 정렬, 10칸)
f"{'hi':<10}"       # 'hi        '  (왼쪽 정렬)
f"{'hi':^10}"       # '    hi    '  (가운데 정렬)

# 콤마 구분 (큰 숫자)
f"{1000000:,}"      # '1,000,000'
```

### 나눗셈 연산자
```python
7 / 2    # 3.5  (실수 나눗셈, Python 기본)
7 // 2   # 3    (정수 나눗셈, 소수점 버림 - Java의 /와 동일)
7 % 2    # 1    (나머지)

# ⚠️ Python //는 음수 방향으로 내림 → Java와 다름
-7 // 2  # -4   (Python: 음수 방향 내림)
# Java:  -7 / 2 = -3 (0 방향 버림)

# 문제에서 "절댓값으로 나눈 후 부호 붙이기" 요구 시
abs(x) // abs(y)             # 절댓값으로 정수 나눗셈
x * y < 0                    # 부호가 다른지 확인 (결과가 음수)
-(abs(x) // abs(y))          # 음수 결과
```

### 형변환
```python
int("3")        # 문자열 → 정수
float("3.14")   # 문자열 → 실수
str(3.14)       # 숫자 → 문자열 (단, 자릿수 고정 안 됨)
```

---

## 2. 조건문

```python
# Java: if (a == b) { } else if (a > b) { } else { }
if a == b:
    print("같다")
elif a > b:      # Java의 else if → Python은 elif
    print("크다")
else:
    print("작다")
```

### 논리 연산자
```python
# Java: &&  ||  !
# Python: and  or  not

if L >= 2.0 and S >= 17:   # Java: L >= 2.0 && S >= 17
    print("통과")
if L < 2.0 or S < 17:      # Java: L < 2.0 || S < 17
    print("탈락")
if not True:                # Java: !true
    print("거짓")
```

### 문자열 비교
```python
# Java: str.equals("hello")
if s == "hello":   # Python은 == 으로 비교
    print("같다")

# 사전순 비교 - Java의 compareTo() 없이 < > 로 바로 비교 가능
"apple" < "banana"   # True  (a가 b보다 사전순 앞)
"juno"  > "inseop"   # True  (j가 i보다 사전순 뒤)

# 활용 예시: 사전순으로 가장 앞선 이름 찾기
if name < winner:    # name이 winner보다 사전순 앞이면
    winner = name
```

### 문자 판별
```python
"A".isupper()    # True  (대문자인지)
"a".islower()    # True  (소문자인지)
"a".isalpha()    # True  (알파벳인지)
"1".isdigit()    # True  (숫자인지)

# 대소문자 변환
"Hello".lower()       # "hello"  (전체 소문자)
"Hello".upper()       # "HELLO"  (전체 대문자)
"hello".capitalize()  # "Hello"  (첫 글자만 대문자)
```

### 문자열 join / capitalize
```python
# join: 리스트를 구분자로 연결 (Java의 String.join()과 동일)
"_".join(["hello", "world"])    # "hello_world"
"".join(["hello", "world"])     # "helloworld"

# capitalize: 첫 글자만 대문자, 나머지 소문자
"hello".capitalize()   # "Hello"

# 리스트 슬라이싱: [시작:끝] (Java의 subList()와 동일)
words = ["a", "b", "c", "d"]
words[1:]    # ["b", "c", "d"]  (1번 인덱스부터 끝까지)
words[:2]    # ["a", "b"]       (처음부터 2번 인덱스 전까지)
words[1:3]   # ["b", "c"]       (1번부터 3번 전까지)
```

### 한 줄 조건문 (삼항 연산자)
```python
# Java: int x = (a > b) ? a : b;
x = a if a > b else b
```

---

## 3. 반복문

### for (순회)
```python
# Java: for (int x : arr) { }
for x in arr:
    print(x)

# Java: for (int i = 0; i < 5; i++) { }
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (간격 2)
    print(i)

for i in range(10, 0, -1): # 10, 9, ..., 1 (역순)
    print(i)
```

### 역방향 순회
```python
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1 (역순)
    print(i)

for i in range(i, 0, -1):   # i에서 1까지 역순 (삽입 정렬에서 자주 사용)
    if arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]  # 두 값 교체 (temp 변수 불필요!)
    else:
        break
```

### 인덱스가 필요 없을 때: `_`
```python
for _ in range(3):   # i 대신 _ 사용 (관례적으로 "안 쓰는 변수"를 의미)
    print("hello")
```

### enumerate / zip
```python
for i, v in enumerate(["a", "b", "c"]):  # 인덱스 + 값
    print(i, v)   # 0 a / 1 b / 2 c

for x, y in zip([1,2,3], ["a","b","c"]):  # 두 배열 동시에
    print(x, y)   # 1 a / 2 b / 3 c
```

### while
```python
# Java: while (true) { }
while True:       # 소괄호 없음, 중괄호 없이 들여쓰기
    break

while i < 5:      # Java: while (i < 5) { }
    i += 1
```

### 반복문 제어
```python
continue   # 이번 반복 건너뜀 (Java와 동일)
break      # 반복문 탈출 (Java와 동일)
```

---

## 4. 배열 (List)

### 선언
```python
arr = []               # 빈 배열
arr = [0, 1, 2, 3]     # 값으로 초기화
arr = [0] * 5          # [0, 0, 0, 0, 0]
arr = [[0]*5 for _ in range(3)]  # 3행 5열 2차원 배열
```

### 인덱싱 / 슬라이싱
```python
arr = [10, 20, 30, 40, 50]
arr[0]     # 10 (첫 번째)
arr[-1]    # 50 (마지막)
arr[1:3]   # [20, 30] (인덱스 1 이상 3 미만)
arr[::-1]  # [50, 40, 30, 20, 10] (역순)
```

### 주요 메서드
```python
arr.append(5)           # 끝에 추가
arr.extend([4, 5, 6])  # 여러 요소 한번에 추가 (append 여러번 대신 사용)
arr.insert(1, 99)       # 인덱스 1 위치에 99 삽입
arr.pop()               # 마지막 요소 제거 후 반환
arr.pop(0)              # 인덱스 0 요소 제거 후 반환
arr.remove(3)           # 값 3 제거 (처음 나오는 것만)
arr.sort()              # 오름차순 정렬 (원본 변경)
arr.sort(reverse=True)  # 내림차순 정렬
sorted(arr)             # 정렬된 새 배열 반환 (원본 유지)
arr.reverse()           # 역순 (원본 변경)
len(arr)                # 길이
sum(arr)                # 합계
arr.count(3)            # 값 3의 개수
arr.index(3)            # 값 3의 인덱스
3 in arr                # 3이 있으면 True
```

### 배열 언패킹 출력
```python
arr = [1, 1, 3, 4, 5]
print(*arr)                        # 1 1 3 4 5  (소규모 배열에 사용)
print(arr)                         # [1, 1, 3, 4, 5]  (대괄호, 쉼표 포함)
print(' '.join(map(str, arr)))     # 1 1 3 4 5  (대규모 배열에 안전)

# * 는 배열을 풀어서 개별 인자로 전달 (n이 클 때 RuntimeError 가능)
# print(*arr) == print(1, 1, 3, 4, 5) 와 동일
```

### 슬라이스 부분 교체
```python
arr = [3, 1, 4, 1, 5, 9, 2]
arr[:3] = sorted(arr[:3])   # 앞 3개만 정렬로 교체
# arr = [1, 3, 4, 1, 5, 9, 2]
```

### 두 값 교체 (swap)
```python
# Java: temp 변수 필요
# int temp = a; a = b; b = temp;

# Python: 한 줄로 가능
a, b = b, a
arr[i], arr[j] = arr[j], arr[i]
```

---

## 5. 딕셔너리 (dict)

> Java의 HashMap과 동일한 개념

### 선언 및 사용
```python
d = {}
d = {"apple": 1, "banana": 2}

d["apple"]          # 1 (키로 값 접근)
d["cherry"] = 3     # 추가
d["apple"] = 10     # 수정
del d["banana"]     # 삭제
```

### 안전하게 접근하기
```python
# Java: map.getOrDefault("key", 기본값)
d.get("apple", 0)   # 없으면 0 반환 (에러 안 남)
d["없는키"]         # KeyError 발생! (위험)
```

### 순회
```python
"apple" in d            # 키 존재 여부
for k in d:             # 키 순회
for k, v in d.items():  # 키-값 동시 순회
len(d)                  # 크기
```

---

## 6. 문자열

### 따옴표: `''` vs `""`
```python
# 둘 다 동일! Java처럼 char/String 구분 없음
'hello' == "hello"   # True

# 문자열 안에 따옴표가 있을 때 구분해서 씀
"I'm happy"          # 안에 '가 있으면 ""로 감싸기
'He said "hello"'    # 안에 "가 있으면 ''로 감싸기
```

### 기본 조작
```python
s = "Hello World"
len(s)        # 11
s[0]          # 'H'
s[-1]         # 'd'
s[0:5]        # 'Hello'
s[::-1]       # 'dlroW olleH' (역순)
```

### 포함 여부 확인 (`in`)
```python
# Java: str.contains("D2")
"D2" in s           # True/False (대소문자 구분)
"d2" in s.lower()   # 소문자로 통일해서 확인

# ⚠️ in의 두 가지 역할
"d2" in s           # → 포함 여부 확인 (True/False 반환)
for x in arr:       # → 순회 대상 지정 (for문 전용)
```

### 주요 메서드
```python
s.upper()           # 대문자 변환
s.lower()           # 소문자 변환
s.split()           # 공백 기준 분리 → ['Hello', 'World']
s.split(",")        # 쉼표 기준 분리
s.strip()           # 앞뒤 공백/줄바꿈(\n) 제거 → sys.stdin.readline 사용 시 필수
s.lstrip("0")       # 왼쪽에서 특정 문자 제거 ("0121" → "121")
s.rstrip()          # 오른쪽 공백 제거
s.replace("l", "r") # 'Herro Worrd'
s.count("l")        # 3 (l의 개수)
s.find("W")         # 6 (인덱스, 없으면 -1)
s.startswith("He")  # True
s.endswith("ld")    # True
"abc".isalpha()     # True (알파벳만)
"123".isdigit()     # True (숫자만)
```

### 문자 ↔ 아스키 코드
```python
ord('A')   # 65
chr(65)    # 'A'
ord('a')   # 97
```

---

## 7. 유용한 내장 함수

```python
abs(-5)           # 5 (절댓값)
pow(2, 10)        # 1024 (거듭제곱)
round(3.14)       # 3 (반올림)

# math 모듈 (import math 필요)
import math
math.ceil(3.2)    # 4  (올림 - Java의 Math.ceil()과 동일)
math.floor(3.8)   # 3  (내림)
math.sqrt(9)      # 3.0 (제곱근)
math.inf          # 무한대 (int 최댓값 대신 사용)

# 올림을 import 없이 수식으로 처리
(7 + 2 - 1) // 2  # 4  (7을 2로 나눠 올림)
# 공식: (값 + 나누는수 - 1) // 나누는수
max(1, 2, 3)      # 3
min(1, 2, 3)      # 1
max([1, 2, 3])    # 배열도 가능
sorted([3,1,2])              # [1, 2, 3]
sorted([3,1,2], reverse=True) # [3, 2, 1]

# 리스트 컴프리헨션
squares = [x**2 for x in range(5)]            # [0, 1, 4, 9, 16]
evens   = [x for x in range(10) if x % 2==0]  # [0, 2, 4, 6, 8]
```

---

## 8. 코테 필수 모듈

### XOR 연산 (`^`)

```python
# XOR: 같은 값이 2번 나오면 상쇄됨 (0이 됨)
# a ^ a = 0
# a ^ 0 = a

1 ^ 1   # 0
3 ^ 3   # 0
1 ^ 3 ^ 3  # 1  (3이 상쇄되고 1만 남음)
4 ^ 4 ^ 10 # 10 (4가 상쇄되고 10만 남음)

# 활용: 짝수번 등장한 값은 모두 상쇄 → 홀수번 등장한 값만 남음
nums = [1, 2, 3, 2, 1]
result = 0
for n in nums:
    result ^= n
# result = 3  (1, 2가 각각 2번 등장해 상쇄)
```

---

### lambda (익명 함수)

```python
# 기본 형태: lambda 파라미터: 반환값
f = lambda x: x * 2
f(3)  # 6

# 주로 sort의 key= 에 사용
arr = [[3, 1], [1, 3], [2, 2]]
arr.sort(key=lambda x: x[1])         # 두 번째 요소 오름차순
arr.sort(key=lambda x: -x[1])        # 두 번째 요소 내림차순
arr.sort(key=lambda x: (x[1], x[0])) # 첫 기준 같으면 두 번째 기준

# max/min에도 사용
max(arr, key=lambda x: x[0])  # 첫 번째 요소가 가장 큰 항목 반환
```

---

### collections.Counter

```python
from collections import Counter

arr = ["a", "b", "a", "c", "a", "b"]
freq = Counter(arr)
# Counter({'a': 3, 'b': 2, 'c': 1})

freq["a"]          # 3 (없는 키는 0 반환, KeyError 없음)
freq.most_common(2) # [('a', 3), ('b', 2)] (많은 순서 상위 2개)

# 두 Counter 교집합 (공통 원소 개수)
c1 = Counter(["a", "b", "a"])
c2 = Counter(["b", "a", "c"])
c1 & c2  # Counter({'a': 1, 'b': 1})
sum((c1 & c2).values())  # 2
```

---

### collections.deque (덱)

**개념**: 편의점 계산대 줄처럼, 먼저 온 사람이 먼저 나감 (FIFO)

```
append(1) → [1]
append(2) → [1, 2]
append(3) → [1, 2, 3]
popleft() → 1 꺼냄, [2, 3] 남음  ← 맨 앞에서 꺼냄!
popleft() → 2 꺼냄, [3] 남음
```

**왜 list 대신 deque?**
`list.pop(0)` 은 뒤 원소를 전부 앞으로 당겨야 해서 O(N)으로 느림.
`deque.popleft()` 는 O(1)로 빠름 → BFS에서 필수.

```python
from collections import deque

# 큐(Queue)로 사용할 때 - list보다 popleft()가 훨씬 빠름
queue = deque()
queue.append(1)    # 오른쪽에 추가: [1]
queue.append(2)    # [1, 2]
queue.popleft()    # 왼쪽에서 꺼냄: 1 반환, [2] 남음

# 스택처럼도 사용 가능
queue.appendleft(0)  # 왼쪽에 추가
queue.pop()          # 오른쪽에서 꺼냄

# 초기값과 함께 생성
queue = deque([1, 2, 3])
```

**자료구조 비교**

| 자료구조 | 꺼낼 때 나오는 것 | 언제 씀 |
|---------|----------------|--------|
| 스택 (list) | 마지막에 넣은 것 (LIFO) | DFS, 괄호 검사 |
| 큐 (deque) | 처음에 넣은 것 (FIFO) | BFS, 순서 처리 |
| 힙 (heapq) | 가장 작은 것 | 우선순위 처리 |

---

### itertools.combinations / permutations

```python
from itertools import combinations, permutations

# combinations: 조합 (순서 무관)
list(combinations([1, 2, 3], 2))
# [(1,2), (1,3), (2,3)]

# permutations: 순열 (순서 고려)
list(permutations([1, 2, 3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# 활용: 조합을 순회하며 조건 체크
for a, b in combinations([1, 2, 3, 4], 2):
    print(a, b)  # 모든 2개 조합
```

---

### heapq (우선순위 큐)

**개념**: 꺼낼 때 항상 가장 작은 값이 나오는 자료구조.
Java의 `PriorityQueue`와 완전히 동일한 개념.

**일반 list와 차이**
```python
# 일반 list - 넣은 순서대로 꺼냄
arr = []
arr.append(5)
arr.append(1)
arr.append(3)
arr.pop()    # 3 (마지막에 넣은 것) ← 최솟값 모름

# heapq - 꺼낼 때 항상 최솟값
import heapq
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappop(heap)    # 1 (가장 작은 값) ← 항상 최솟값!
heapq.heappop(heap)    # 3
heapq.heappop(heap)    # 5
```

**내부 동작 (이진 트리 구조)**
```
heappush(5) →   5

heappush(1) →   1     ← 1이 5보다 작으니까 위로 올라옴
               /
              5

heappush(3) →   1
               / \
              5   3

heappop()   →   3     ← 1 꺼내고, 내부적으로 재정렬
               /
              5
```
핵심: 내부 구조 몰라도 됨. **heappush로 넣으면 → heappop할 때 항상 최솟값**이 나온다는 것만 기억.

```python
import heapq

heap = []
heapq.heappush(heap, 3)    # 추가
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappop(heap)         # 1 반환 (가장 작은 값)

heap[0]                     # 현재 최솟값 확인 (꺼내지 않음)

# 최대 힙: 음수로 넣으면 됨 (Python엔 max-heap이 없음)
heapq.heappush(heap, -5)
-heapq.heappop(heap)        # 5 반환

# 리스트를 힙으로 변환
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)          # arr 자체가 힙 구조로 변환됨
```

**Java 비교**
```java
// Java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(5);
pq.offer(1);
pq.poll();  // 1 (최솟값)
```
```python
# Python - 완전히 동일
import heapq
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappop(heap)  # 1 (최솟값)
```

**언제 씀?** 매번 가장 작은(또는 큰) 값을 꺼내야 할 때.
예: 최단 경로(다익스트라), 작업 우선순위 처리

---

### collections.defaultdict

Java의 `map.getOrDefault()` 를 매번 쓰지 않아도 됨. 없는 키에 접근하면 자동으로 기본값 생성.

```python
from collections import defaultdict

# int: 없는 키는 0으로 초기화
d = defaultdict(int)
d["a"] += 1    # KeyError 없이 바로 사용 가능
d["b"] += 3
# d = {'a': 1, 'b': 3}

# list: 없는 키는 []로 초기화
d2 = defaultdict(list)
d2["a"].append(1)
d2["a"].append(2)
# d2 = {'a': [1, 2]}

# 일반 dict와 차이
d3 = {}
d3["x"] += 1   # KeyError 발생!

d4 = defaultdict(int)
d4["x"] += 1   # 0 + 1 = 1, 정상 동작
```

---

### bisect (이분탐색)

정렬된 배열에서 삽입 위치를 O(log N)으로 찾음. Java의 `Collections.binarySearch()` 보다 더 유연함.

```python
import bisect

arr = [1, 3, 5, 7, 9]  # 반드시 정렬된 상태여야 함

bisect.bisect_left(arr, 5)   # 2 (5가 들어갈 왼쪽 위치, 5 포함)
bisect.bisect_right(arr, 5)  # 3 (5 오른쪽 위치, 5 미포함)

bisect.bisect_left(arr, 4)   # 2 (4가 들어갈 위치)
bisect.bisect_left(arr, 6)   # 3 (6이 들어갈 위치)

# 활용: 정렬 유지하며 삽입
bisect.insort(arr, 4)        # arr = [1, 3, 4, 5, 7, 9]

# 활용: 특정 값이 배열에 있는지 확인
idx = bisect.bisect_left(arr, 5)
if idx < len(arr) and arr[idx] == 5:
    print("5 있음")
```

---

### sys.setrecursionlimit (재귀 깊이 설정)

Python 기본 재귀 깊이는 1000. DFS나 DP를 재귀로 구현할 때 늘려야 함.

```python
import sys
sys.setrecursionlimit(10**6)  # 파일 최상단에 한 번만 선언
```

---

## 9. 유형별 자주 쓰는 문법

### A. 완전탐색 / 브루트포스
```
combinations, permutations → 모든 조합/순열 생성
for + if → 조건 만족하는 경우 탐색
```
```python
from itertools import combinations

for a, b in combinations(arr, 2):   # 2개 조합
    if a + b == target:
        count += 1
```

---

### B. BFS (너비 우선 탐색)
```
deque → 큐 역할 (popleft가 핵심)
visited set → 방문 체크
```
```python
from collections import deque

queue = deque([(시작x, 시작y)])
visited = set()
visited.add((시작x, 시작y))

while queue:
    x, y = queue.popleft()
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:  # 상하좌우
        nx, ny = x+dx, y+dy
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            queue.append((nx, ny))
```

---

### C. DFS (깊이 우선 탐색)
```
재귀 + sys.setrecursionlimit → 깊은 재귀
stack(list) → 반복문으로 구현 시
```
```python
import sys
sys.setrecursionlimit(10**6)

def dfs(node, visited):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, visited)
```

---

### D. 정렬
```
lambda → 커스텀 정렬 기준
sorted() → 원본 유지
```
```python
arr.sort(key=lambda x: (-x[1], x[0]))  # 두 번째 내림차순, 같으면 첫 번째 오름차순
```

---

### E. 해시 / 빈도 계산
```
Counter → 빈도 세기
defaultdict → 그룹핑
dict → 값 매핑
```
```python
from collections import Counter, defaultdict

freq = Counter(arr)              # 빈도 계산
groups = defaultdict(list)       # 키별 그룹핑
for v in arr:
    groups[v % 2].append(v)     # 짝수/홀수 그룹
```

---

### F. 우선순위 큐 (최솟값/최댓값 반복 추출)
```
heapq → 정렬 없이 항상 최솟값 O(log N)
```
```python
import heapq

heap = []
for v in arr:
    heapq.heappush(heap, v)

result = heapq.heappop(heap)    # 가장 작은 값
```

---

### G. 이분탐색
```
bisect → 정렬된 배열에서 위치 탐색
```
```python
import bisect

arr.sort()
pos = bisect.bisect_left(arr, target)   # target의 위치
count = bisect.bisect_right(arr, target) - bisect.bisect_left(arr, target)  # target 개수
```

---

### H. DP (동적 프로그래밍)
```
list → dp 테이블
점화식 → dp[i] = dp[i-1] + ...
```
```python
dp = [0] * (N + 1)
dp[0] = 초기값
dp[1] = 초기값
for i in range(2, N + 1):
    dp[i] = dp[i-1] + dp[i-2]   # 점화식
```

---

### I. 문자열 처리
```
split / join → 분리 및 합치기
Counter → 문자 빈도
슬라이싱 → 부분 문자열
```
```python
s[::-1]                  # 역순
s.split()                # 공백 기준 분리
"_".join(words)          # 리스트 → 문자열
Counter(s)               # 문자 빈도
s[i:j]                   # 부분 문자열
```
