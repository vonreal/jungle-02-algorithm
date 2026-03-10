# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

'''
# 개선 풀이 , 피드백 with AI
# 달라진 점 -> 문제의 단위: 블록 단위로 잡기

Ideas
    1. '::' 기준으로 왼쪽, 오른쪽 블록을 판단하기
    2. 빈 블록은 '0000'채워주기
    3. 각 블록을 4자리로 맞춰주기 1 -> 0001
    4. ':'로 합치기
'''
before_ipv6 = input().strip()
origin_ipv6 = []

def fill_block(target):
    if not target:
        return []
    return [ele.zfill(4) for ele in target.split(':')]

if '::' in before_ipv6:
    left_blocks, right_blocks = before_ipv6.split('::')

    left = fill_block(left_blocks)
    right = fill_block(right_blocks)

    empty_block_count = 8 - (len(left) + len(right))
    origin_ipv6 = left + ['0000'] * empty_block_count + right
else:
    origin_ipv6 = fill_block(before_ipv6)

print(":".join(origin_ipv6))

# 파이써닉한 방법

s = input().strip()

if '::' in s:
    left, right = s.split("::")
    left_parts = left.split(":") if left else []
    right_parts = right.split(":") if right else []
    missing = 8 - (len(left_parts) + len(right_parts))
    parts = left_parts + ['0'] * missing + right_parts
else:
    parts = s.split(":")
    
print(':'.join(part.zfill(4) for part in parts))

'''
# 첫 풀이
# 현재는 문제의 단위를 문자로 잡고 있음. 그래서 디버깅이 더 어려운 문제가 발생함.
# 또 split을 ':'로 보고 있는데 그러면 '::'일때 추가 처리가 필요해짐.

before_ipv6 = input().split(':')
origin_ipv6 = list('0000:0000:0000:0000:0000:0000:0000:0000')

current_index = 0
flag = False

for index, ipv6 in enumerate(before_ipv6):
    if not flag and ipv6 == '':
        current_index += abs(5 * (8 - len(before_ipv6) + 1))
        flag = True
        continue

    for i, c in enumerate(reversed(ipv6)):
        if c == '':
            continue
        origin_ipv6[current_index + (3 - i)] = c
    current_index += 5

print("".join(origin_ipv6))
'''

'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> IPv6 주소 최대 39글자

        -> 앞자리의 0의 전체 또는 일부를 생략 할 수 있다.
        -> 0으로만 이루어져 있는 그룹은 한 개 이상 연속된 그룹을 :: 콜론 2개로 바꿀 수 있다.
    2) 출력범위
        -> 40글자의 축약되지 않은 형태
    3) Brute Force 가능한가?

2. Ideas
    1) 
        0000:0000:...:0000 으로 초기화 된 32자리 + ':' 8자리 원본 데이터를 선언한다.
        입력값을 ':'기준으로 split해서 2차원 배열로 저장한다.
        
        ':'이 나올때까지 읽고 index 기반으로 값을 대입해준다.
        ':'이 나오고 ''을 읽었다면 8 - 현재 before_ipv6의 길이 - 처리한 구간을 해서 그만큼 구간을 건너뛴다.

3. Complexities
    Idea 1) 

4. Code
5. Test

6. 개선 포인트 with AI
'''