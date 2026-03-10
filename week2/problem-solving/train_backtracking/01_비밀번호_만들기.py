# 순열

# 숫자 [1, 2, 3]으로 만들 수 있는 모든 3자리 비밀번호를 구하라.
# 각 숫자는 한 번씩만 사용 가능.

# 입력 크기는 3
# 모든 조합 검사
# 순서 중요 -> 1,2,3, 3,2,1 은 다른 값 -> 순열 O(N!)
# 각 숫자는 한 번 씩만 사용 가능 백트래킹

nums = input().split()
result = []

def backtrack(path):
    if len(path) == len(nums):
        result.append(int("".join(path)))
        return
    
    for num in nums:
        if num in path:
            continue
        
        path.append(num)
        backtrack(path)
        path.pop()

backtrack([])
print(result)