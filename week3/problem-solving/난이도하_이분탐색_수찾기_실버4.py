# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

_ = int(input())
nums = [int(n) for n in input().split()]

_ = int(input())
targets = [int(n) for n in input().split()]

# 해시 집합 set 사용
def idea2():
    hash_nums = set(nums)
    result = ('1' if target in hash_nums else '0' for target in targets)
    print("\n".join(result))

# binary search 사용
def idea1():
    result = []

    def binary_search(sorted_nums, target):
        left = 0
        right = len(sorted_nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if sorted_nums[mid] == target:
                return True
            elif sorted_nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

    sorted_nums = sorted(nums)

    for target in targets:
        if binary_search(sorted_nums, target):
            result.append('1')
        else:
            result.append('0')

    print("\n".join(result))

idea2()


'''
1. Constraint
    - N, M <= 100,000
    - O(N^2) 불가능
    - O(N log N) 또는 O(N + M) 정도 목표

2. Idea / Complexity
    1) 이분 탐색
        - nums 정렬: O(N log N)
        - 각 target마다 이분 탐색: O(M log N)
        = 총 시간복잡도: O(N log N + M log N)
        = 추가 공간복잡도: O(N + M)

    2) 해시 집합(set)
        - nums를 set으로 변환: O(N)
        - 각 target 조회: 평균 O(M)
        = 총 시간복잡도: 평균 O(N + M)
        = 추가 공간복잡도: O(N + M)
'''