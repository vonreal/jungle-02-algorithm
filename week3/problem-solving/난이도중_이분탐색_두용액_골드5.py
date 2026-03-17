# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
import sys
from bisect import bisect_left
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

# 핵심연산: 하나를 pick 했을때 pick한 것의 합이 0이 되게 만드는 가장 이상적인 짝꿍 -pick을 찾는 것 (혹은 그에 수렴하는 것)
def custom_bisect_left(datas, target, lo):
    left = lo
    right = len(datas) - 1
    while left < right:
        mid = (left + right) // 2
        
        if datas[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def solve_binary_search():
    min_sum = float('inf')
    answers = [0, 0]

    for i in range(N - 1):
        target = -datas[i]

        # idx = bisect_left(datas, target, lo=i+1)
        idx = custom_bisect_left(datas, target, lo=i+1)

        if idx < N:
            current_sum = datas[i] + datas[idx]
            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                answers = [datas[i], datas[idx]]
        
        if idx - 1 > i:
            current_sum = datas[i] + datas[idx - 1]
            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                answers = [datas[i], datas[idx - 1]]

    print(answers[0], answers[1])

solve_binary_search()

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