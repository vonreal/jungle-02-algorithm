# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

# Answer 코드
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(9)]

max_num = 0
max_index = 0

for index, num in enumerate(nums):
    if max_num < num:
        max_num = num
        max_index = index + 1

print(max_num, max_index, sep='\n')

'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> 항상 9개(O(1)), 각 자연수는 1부터 100까지
    2) 출력범위
        -> 정수 2개: 최댓값, 몇번째인지
    3) Brute Force 가능한가?
        -> 가능함 항상 9개만 비교하면 되기 때문

2. Ideas
    1) 전체를 돌면서 최댓값, 최댓값의 index를 비교 후 업데이트 해준다.
    2) Python의 내장함수 max와 .index 메서드를 사용한다.
        max() 시간복잡도 O(N)
        .index() 시간복잡도 O(N)

3. Complexities
    Idea 1) 시간복잡도 O(N) -> 근데 N은 항상 9니까 O(1), 공간복잡도 O(1): 변수만 새로 생성
    Idea 2) 시간복잡도 O(2N) -> O(N), 공간복잡도 O(1)

4. Code
5. Test

6. 개선 포인트 with AI
'''

def pythonic_solution1():
    nums = [int(input()) for _ in range(9)]
    max_num = max(nums)
    max_index = nums.index(max_num) + 1
    print(max_num, max_index, sep='\n')

def pythonic_solution2():
    nums = [int(input()) for _ in range(9)]
    max_index, max_num = max(enumerate(nums), key=lambda x: x[1])
    print(max_num, max_index, sep='\n')