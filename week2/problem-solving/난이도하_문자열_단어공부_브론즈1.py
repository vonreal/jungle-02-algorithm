# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

import sys
from collections import Counter
input = sys.stdin.readline

def sol3(): 
    string = input().upper()
    top_two = Counter(string).most_common(2)

    if len(top_two) > 1 and top_two[0][1] == top_two[1][1]:
        print('?')
    else:
        print(top_two[0][0])

def sol2():
    # sys.stdin.readline()은 개행 문자 '\n'이 포함됨
    # word = input().upper()
    word = input().strip().upper()

    if word == '':
        return

    cnt = [0] * 26

    for char in word:
        cnt[ord(char) - ord('A')] += 1

    mx = max(cnt)

    if cnt.count(mx) > 1:
        print("?")
    else:
        print(chr(cnt.index(mx) + ord('A')))

sol2()

'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

시간 제한: 2초 (2000만번)

1. Constraints
    1) 입력범위
        -> 단어가 주어짐 단어는 1,000,000 이하
    2) 출력범위
        -> 가장 많이 사용된 알파벳(대소문자 구분 x) 대문자로 출력, 여러 개 존재 시 ? 출력  (변수 한개로 종결)
    3) Brute Force 가능한가?
        -> 불가능 O(N^2) 미만이어야함

2. Ideas
    1) ❌ max 내장함수 사용 -> O(N)
        - 소문자 혹은 대문자로 처리 필요함 .lower() / .upper() -> O(N)
        - 같을 경우 처리가 어떻게 되는가? -> 복수 존재 시 첫 번째 반환
        => max가 여러번 나타나는 걸 표현하는게 아니라 아스키 값 중 가장 큰 것을 의미함
    2) 아스키로 값 비교? 'a' - 'A' = 32
        - a~z (26) 배열 생성해서 값 올려서 max로 찾기?
    3) Coutner 객체 활용하기 -> (O(N))
        - 가장 빈도수가 높은 요소 most_common(k) -> O(N log k)
        - 같을 경우 어떻게 처리되는가? 
    4) Dic 사용

3. Complexities
    Idea 2)
        - 시간복잡도: O(N + N + N) -> O(N)
        - 공간복잡도: O(26) -> O(1)
    Idea 3)
        - 시간복잡도: O(N + N log k) -> O(N + N log 2) -> O(N + N) -> O(2N) -> O(N)
        - 공간복잡도: O(26) -> O(1)

4. Code
5. Test
6. pain point
처음에는 코드를 아래처럼 풀었는데 예제로 주어진 테스트케이스 'z'만 생각해서 'zZz'이런식으로 넘어오는 걸 고려하지 못했다.
그래서 'Z'가 나와야하는데 'zZz'가 나와서 이 부분을 조금 헤맸었다. (AI한테 내가 틀릴 수 있는 테스트케이스 알려달라해서 깨달음)

string = input().upper()
top_two = Counter(string).most_common(2)

if len(top_two) > 1:
    if top_two[0][1] == top_two[1][1]:
        print('?')
    else: 
        print(top_two[0][0])
else: 
    print(string)

7. 개선 포인트 with AI
'''