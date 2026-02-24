# 코딩테스트 Python 문법 정리 (Java 비교)

## 목차
1. [입출력](#1-입출력)
2. [조건문](#2-조건문)
3. [반복문](#3-반복문)
4. [배열 (List)](#4-배열-list)
5. [딕셔너리 (dict)](#5-딕셔너리-dict)
6. [문자열](#6-문자열)
7. [유용한 내장 함수](#7-유용한-내장-함수)

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

### 문자열 비교
```python
# Java: str.equals("hello")
if s == "hello":   # Python은 == 으로 비교
    print("같다")
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
s.strip()           # 앞뒤 공백 제거
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
max(1, 2, 3)      # 3
min(1, 2, 3)      # 1
max([1, 2, 3])    # 배열도 가능
sorted([3,1,2])              # [1, 2, 3]
sorted([3,1,2], reverse=True) # [3, 2, 1]

# 리스트 컴프리헨션
squares = [x**2 for x in range(5)]            # [0, 1, 4, 9, 16]
evens   = [x for x in range(10) if x % 2==0]  # [0, 2, 4, 6, 8]
```
