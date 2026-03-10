# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
import sys

MAX = 10000

input = sys.stdin.readline

T = int(input())
is_primes = [True] * (MAX + 1)
is_primes[0] = is_primes[1] = False

for num in range(2, int(MAX ** 0.5) + 1):
    if is_primes[num]:
        for i in range(num*num, MAX + 1, num):
            is_primes[i] = False

for _ in range(T):
    N = int(input())

    half = N // 2

    for i in range(half, 0, -1):
        if not is_primes[i]:
            continue

        if not is_primes[N - i]:
            continue

        print(i, N-i)
        break


'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> 짝수 n , 최솟값:4, 최댓값: 10,000
        -> 테스트 케이스 개수 T 제한 없음
    2) 출력범위
        -> n의 골드바흐 파티션 출력, 단 여러개일 경우 소수의 차이가 가장 작은 것 출력, 작은 소수 부터 출력, 공백 구분
    3) Brute Force 가능한가?
        -> 놉

2. Ideas
    1)
        - 최댓값이 10,000이니 미리 10,000의 제곱근(100)까지의 소수를 배열에 담아놓는다. 에라~채 이용
        - 주어진 수를 절반으로 나누고 인접한 소수를 찾는다.
            ex) 10 -> 10/2 = 5  5는 소수인가? -> yes 5의 조합 찾기
            ex) 8 -> 8/2 = 4 4는 소수인가? -> no 4-1 = 3 -> 3은 소수인가? yes 그럼 8-3=5 5는 소수인가? No -> 4 + 1 = 5 이런식으로?
                -> 절반을 나눈 숫자가 소수일때까지 (선택)
                -> 2번째 숫자 선택 (N-(위에서 선택한 수)) -> 없으면 다시 돌아가서 -1


3. Complexities
    Idea 1) 
        - 시간복잡도: O(100)
        - 공간복잡도: O(100)

4. Code
5. Test

6. 개선 포인트 with AI
'''