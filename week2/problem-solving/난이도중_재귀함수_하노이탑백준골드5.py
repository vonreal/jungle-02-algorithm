# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

N = int(input())

count = 0
orders = []

def move(N, x, y):
    global count

    count += 1

    if N > 1:
        move(N-1, x, 6 - x - y)
    
    if N <= 20:
        orders.append([x, y])

    if N > 1:
        move(N-1, 6 - x - y, y)

move(N,1,3)

print(count)
if orders:
    print('\n'.join(f"{a} {b}" for a, b in orders))


'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> N: 첫 번째 장대에 쌓인 원판의 개수 최솟값: 1, 최댓값: 100
    2) 출력범위
        -> 첫째 줄에 옮긴 횟수 K
        -> 두번째 줄부터 k개의 줄에 걸쳐 두 정수 빈칸을 두고 출력, A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다.
            N이 20이하일때만 출력
    3) Brute Force 가능한가?
        -> 

2. Ideas
0.    1) 

3. Complexities
    Idea 1) 

4. Code
5. Test

6. 개선 포인트 with AI
'''