# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
import sys
input = sys.stdin.readline
_ = input()

tops = [int(top) for top in input().split()]

stack = []
result = []

for seq, top in enumerate(tops, 1):
    while stack and stack[-1][1] < top:
        stack.pop()

    if not stack:
        result.append('0')
    else:
        result.append(str(stack[-1][0]))

    stack.append((seq, top))

print(" ".join(result))
     
    
'''
스택

0. 조건
    시간제한: 1.5초 (1500만번)

1. Constraints
    1) 입력범위
        -> 탑의 수를 나타내는 정수 N (1~500,000)
        -> 탑의 높이 (1~100,000,000)
    2) 출력범위
        -> N개의 결과가 나와야 하고 하나의 정수는 0 ~ 499,999를 가짐
        -> 결과는 탑의 번호임. 근데 번호는 1부터 시작함.
2. Ideas
    1) 모든 요소를 순회하면서 n-1개와 비교하면서 카운팅한다.
    2) 스택으로 모든 데이터를 넣고 뒤에서부터 pop하면서 수신하는 탑의 번호를 출력한다. ---> 근데 이러면 굳이 스택을 써야하나?
        -> 이때 출력은 1번 탑부터 진행되어야 하기 때문에. 데이터를 역순으로 진행한다.
    3) 모든 요소를 순회하면서 수신 가능한 탑만 stack에 넣고, 수신 불가능한 탑은 pop()처리한다.

- 가지치기
    0) 탑은 항상 자기랑 같거나 높은 탑에서만 수신가능함. -> 수신한 탑이 존재하면 끝임
    1) 첫번째 탑은 항상 0

3. Complexity
    Idea 1, 2) 
        시간복잡도: O(n*n-1) => O(n^2) 불가능
    Idea 3)

'''