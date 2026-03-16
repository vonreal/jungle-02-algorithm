# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
import sys
import bisect
input = sys.stdin.readline

N = int(input())
datas = list(map(int, input().split()))
datas.sort() # O(N log N)

def solve_two_pointer():
    # 1. 오른쪽 끝에서 하나의 용액을 선택한다.
    # 2. 왼쪽 끝에서 하나의 용액을 선택한다.
    # 3. 두 개를 합한다.
        # 최솟값이라고 가정하고 저장한다.
        # 최솟값이 있으면 비교해서 더 0에 가까운 수라면 최솟값과 select_nums를 업데이트한다.
    # 언제까지? 두 개의 인덱스가 만나거나 한 쪽이 넘어설 때까지

    min_sum = float('inf')
    min_select_nums = [None, None]

    i = 0
    j = len(datas) - 1
    while True:
        if i >= j:
            break
        sum_two_data = datas[i] + datas[j]
        if abs(min_sum) > abs(sum_two_data):
            min_sum = sum_two_data
            min_select_nums[0], min_select_nums[1] = datas[i], datas[j]
        if sum_two_data > 0:
            j -= 1
        else:
            i += 1

    print(*min_select_nums)

def solve_binary_search():
    # 1. 하나의 용액을 선택한다.

    pass

solve_two_pointer()

'''
시간 제한: 1초
메모리 제한: 128 MB

1. Constraints
    -> 전체 용액의 수: N (2 ~ 100,000)
    -> 용액의 특성값을 나타내는 정수
    출력범위: 

2. Ideas
    핵심연산: 두 값을 더했을때 0에 가장 가까운 두 용액
    연산횟수: 비교가 O(N log N) 혹은 O(N)으로 끝나야 가능함
    -> 하나의 용액에 대해 (N-1)의 경우를 더해봐야 알 수 있지 않나?

    -> 정렬을 먼저 해야함 O(N log N)
    -> 정렬된 배열에서 양 끝을 비교하면서 0에 가까운 두 용액을 찾는다. (투 포인터) O(N)
   
     -> 정렬된 배열에서

'''