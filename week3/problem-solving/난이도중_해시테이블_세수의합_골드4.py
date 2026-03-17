# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
import sys
input = sys.stdin.readline

N = int(input())
u_nums = [int(input()) for _ in range(N)]
u_nums.sort() # O(N log N)

two_sums = set()

# O(N^2)
for index, num in enumerate(u_nums):
    for j in range(index, len(u_nums)):
        two_sums.add(num+u_nums[j])

'''
itertools 활용
from itertools import combinations_with_replacement

two_sums = {a + b for a, b in combinations_with_replacement(u_nums, 2)}
'''

def find_k(nums):
    # 1. k를 정한다. O(N^2)
    for i in range(N-1, -1, -1):
        k = nums[i]
        # 2. z를 정한다.
        for j in range(i-1, -1, -1):
            z = nums[j]
            # 3. k - z와 같은 x + y를 구한다.
            if (k - z) in two_sums:
                return k

# 최대 2,001,000 연산
print(find_k(u_nums))


'''
시간 제한: 1초
메모리 제한: 128 MB

0. 조건
    - x, y, z, k 모두 U 안에 있음
    - 같은 수를 여러번 써도 됨
    - k도 배열 안에 있어야 함
1. Constraints
    입력범위
        - N개의 자연수들로 이루어진 집합 U : N (5 ~ 1,000)
        - 각 원소는 2억보다 작거나 같음
    출력범위
        - 어떤 수 x + y + z = k 일때 가장 큰 k를 출력하기
2. Ideas
    핵심연산: 현재는 세 수의 합 O(N^3)이 되어버림
    연산횟수: 
    
    1)  x + y = k - z
     -> x + y는 two sum 풀이 처럼 진행하면 됨 --> 놉 그냥 미리 조합을 다 만들어놓기.
     -> k는 정렬된 배열에서 가장 큰 수부터 선택하고, z는

3. Complexity
    Ideas 1)
        시간복잡도: O(N^2)
        공간복잡도: O(N^2) - two_sums set 크기
'''