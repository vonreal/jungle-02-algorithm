# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
import sys
input = sys.stdin.readline

N = int(input())
origin_square = [[int(row) for row in input().split()] for _ in range(N)]

color_square_total = [0, 0]

# 1. 현재 요소가 모두 같은가?
def is_same_elements(x, y, size):
    first_color = origin_square[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if origin_square[i][j] != first_color:
                return False, first_color

    return True, first_color

# 2. 같지 않으면 절반으로 쪼개고, 다시 탐색한다. True면 카운트 1, 더이상 쪼개지 않을 때까지
def divide_square(x, y, size):
    is_same, color = is_same_elements(x, y, size)

    if is_same:
        color_square_total[color] += 1
        return
    
    half = size // 2
    divide_square(x, y, half)
    divide_square(x, y+half, half)
    divide_square(x+half, y, half)
    divide_square(x+half, y+half, half)

divide_square(0,0,N)

print(color_square_total[0], color_square_total[1], sep='\n')

'''
제한사항
    시간제한: 1초
    메모리제한: 128 MB

0. 조건
    - 다양한 크기를 가진 정사각형 모양의 하얀색, 파란색 색종이
    - 정사각형의 조건 가로 = 세로 (가로x세로)

1. Constraints
    - 입력범위: 한 변의 길이 N (2,4,6,8,16,32,64,128)
    - 출력범위: 하얀색 색종이의 개수, 파란색 색종이의 개수 -> 변수 2개로 관리

2. Ideas
    핵심연산: 계속 2/N으로 쪼갠다. 한개가 남거나 혹은 모든 요소가 같을때까지 (재귀, 분할)
    1) 현재 정사각형에서 같은 번호가 아니면 현재 정사각형을 절반으로 쪼갠다.
        -> O(N^2)

3. Complexity
    1) N^2 * log N ?
    공간복잡도는 처음에 입력값 제외 딱히 없음, color담는 (2)
'''

