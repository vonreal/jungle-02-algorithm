# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

N = int(input())

datas = []

for _ in range(N):
    parts = input().split()
    fun, x = parts[0].strip(), int(parts[1]) if len(parts) > 1 else None

    if fun == 'push':
        datas.append(x)
    elif fun == 'pop':
        if not datas:
            print(-1)
            continue
        print(datas.pop())
    elif fun == 'size':
        print(len(datas))
    elif fun == 'empty':
        if not datas:
            print(1)
        else:
            print(0)
    elif fun == 'top':
        if not datas:
            print(-1)
            continue
        print(datas[len(datas) - 1])


'''
새로운 지식: LEGB 규칙

0. 제한
    시간 제한: 0.5초
    메모리 제한: 256MB

1. Constraints
    1) 입력범위
        -> 명령의 수: N / 최소 1 ~ 최대 10,000
        -> 정수: X / 최소 1 ~ 최대 100,000 (정수라서 큰 관계 x)
    2) 출력범위
        -> (N - push 연산 갯수)줄의 결과가 나와야 함
        -> 백준 정의
            pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            size: 스택에 들어있는 정수의 개수를 출력한다.
            empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
            top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
2. Ideas
    1) stack은 동적배열 (list)로 구현한다.
        -> concrete collection
        -> list.append(X) -> list에 마지막에 추가하는 것은 Amortized O(1) (애머타이즈드)
        -> list.pop() -> O(1) 항상 마지막 원소를 빼기 때문
        -> len(list) -> list의 len은 항상 파이썬 객체에 저장된 값이기 때문에 O(1)
        -> list[index] -> O(1) 인덱스 탐색은 항상 O(1)
    2) 입력에서의 명령어를 어떻게 parsing하고 함수 호출로 처리할 것인가?
        -> N만큼 반복문을 돈다.
        -> input().stripe().split()을 해서 문자열로 비교한다.
        -> 이때 기본 명령어에 해당하는 문자열은 매크로 처리
        -> 각 명령어에 맞는 함수를 구현. --> 함수로 처리하면 time exceed, 함수로 빼지 않고 처리하기

3. Complexity
    Idea 1)
        -> 시간복잡도: O(1)
        -> 공간복잡도: O(1)


Python(CPython)은 list의 capacity를 관리하고 있음
대략 1.125배 + 6 정도 왜? -> 메모리 낭비 최소화

import sys

lst = []
prev_size = 0

for i in range(20):
    lst.append(i)
    curr_size = sys.getsizeof(lst)
    if curr_size != prev_size:
        print(f"len={len(lst)}, 메모리={curr_size}바이트")
        prev_size = curr_size
'''