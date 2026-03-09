# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

N = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def answer(n, under_scores):
    print(f'{under_scores}"재귀함수가 뭔가요?"')
    
    if n == 0:
        print(f'{under_scores}"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(f'{under_scores}라고 답변하였지.')
        return
    
    print(f'{under_scores}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f'{under_scores}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(f'{under_scores}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    
    answer(n - 1, under_scores + '____')
    print(f'{under_scores}라고 답변하였지.')

answer(N, '')


'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> N: 재귀 횟수 (1~50)
    2) 출력범위
        -> 문자열을 출력해야함
    3) Brute Force 가능한가?
        -> 가능

2. Ideas
    1) s를 하나씩 읽으면서 출력은 r번 반복한다.

3. Complexities
    Idea 1) 시간복잡도: O(r x s) -> 근데 최대가 160이기 때문에 거의 O(1), 공간복잡도: O(1) 선언하는 변수 없음.

4. Code
5. Test

6. 개선 포인트 with AI
'''