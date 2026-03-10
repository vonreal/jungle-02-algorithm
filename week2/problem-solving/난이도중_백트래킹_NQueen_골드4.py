# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

N = int(input())

count = 0

def existedDiagonal(row, col, selected_col):
    if not selected_col:
        return False
    
    for row2, col2 in enumerate(selected_col):
        if abs(row-row2) == abs(col-col2):
            return True
    return False

def backtrack(row, selected_col):
    global count

    if N == row:
        count += 1
        return
    
    for col in range(N):
        if col in selected_col:
            continue
        
        if existedDiagonal(row, col, selected_col):
            continue

        selected_col.append(col)
        backtrack(row + 1, selected_col)
        selected_col.pop()

backtrack(0, [])
print(count)

'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

제한시간: 10초

0. 선수지식
    1) 퀸의 공격 범위 in chess
        : 퀸은 상하좌우 + 대각선 방향으로 몇 칸이든 이동 가능
        즉, 같은 행, 열, 대각선에 퀸이 없어야 함.

1. Constraints
    1) 입력범위
    2) 출력범위
    3) Brute Force 가능한가?

2. Ideas
    1) 

3. Complexities
    Idea 1)

4. Code
5. Test

6. 개선 포인트 with AI
'''