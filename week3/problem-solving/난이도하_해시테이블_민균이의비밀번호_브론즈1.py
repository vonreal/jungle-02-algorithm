# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys
input = sys.stdin.readline

N = int(input())

def check_password():
    words = set()

    for _ in range(N):
        word = input().strip()
        reverse_word = word[::-1]

        if reverse_word == word:
            return word
        
        if reverse_word in words:
            return word
        
        words.add(word)

password = check_password()
print(len(password), password[len(password) // 2])

'''
시간 제한: 1초
메모리 제한: 128 MB

1. Constraints
    입력
        -> 단어의 수 N (2 ~ 100)
        -> 단어의 길이 (2 ~ 14 사이의 홀수)
    출력
        -> 비밀번호의 길이
        -> 가운데 글자 출력

2. Idea
    1) 모든 글자의 ordinary 를 더해서 map에 저장한다?
    2) 현재 단어에서 뒤집혀진 단어가 맵에 있는지 체크하기 있으면 그게 비밀번호, 아니면 단어를 맵에 추가해본다.
'''