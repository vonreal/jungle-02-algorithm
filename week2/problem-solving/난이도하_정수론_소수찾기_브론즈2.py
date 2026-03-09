# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
import sys
input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))

max_num = max(nums)

prime_check_nums = [True] * (max_num + 1)
prime_check_nums[0] = prime_check_nums[1] = False

for num in range(2, int(max_num**0.5) + 1):
    if prime_check_nums[num]:
         for i in range(num * num, max_num + 1, num):
              prime_check_nums[i] = False

print(sum(prime_check_nums[num] for num in nums))


'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

제한시간: 2초 (2000만번)

1. Constraints
    1) 입력범위
        -> N: 주어진 숫자 (최대 100개)
        -> 숫자는 최대 1000이다.
    2) 출력범위
        -> 소수의 개수 출력
    3) Brute Force 가능한가?
        -> 100 x 1000 = 100000 가능

2. Ideas
    1) 에라토스테네스의 채 사용
    2) 하나씩 소수 판별(제곱근까지) -> 입력값 최대여도 시간안에 가능해서 가능함.

3. Complexities
    Idea 1)
        M: 입력값의 최댓값
        시간복잡도: O(M log log M + N)
        공간복잡도: O(M)
    Idea 2)
        시간복잡도: O(N √M)
        공간복잡도: O(1)

4. Code
5. Test

+ 새로 알게 된 Point
1)'에라토스테네스의 채'의 개념을 얼핏 알고 있어서 해당 개념을 사용해보았다.
이때 배수를 지우는 부분에서 'for i in range(num * 2, max_num + 1, num):'를 했는데 '2'는 이미 2의 배수이기 때문에 지워졌다고 가정한다면
시작은 num * num 부터 하는게 맞다는 부분

6. 개선 포인트 with AI
'''