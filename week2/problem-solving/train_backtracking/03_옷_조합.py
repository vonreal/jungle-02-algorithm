# 단계별 다른 풀

# 상의, 하의, 신발에서 각각 하나씩 골라 코디를 완성하라.

# Example 1:
# Input: 
#   tops = [흰셔츠, 검정셔츠]
#   bottoms = [청바지, 면바지, 반바지]
#   shoes = [운동화, 구두]
# Output: [
#   흰셔츠-청바지-운동화, 흰셔츠-청바지-구두,
#   흰셔츠-면바지-운동화, 흰셔츠-면바지-구두,
#   흰셔츠-반바지-운동화, 흰셔츠-반바지-구두,
#   검정셔츠-청바지-운동화, 검정셔츠-청바지-구두,
#   검정셔츠-면바지-운동화, 검정셔츠-면바지-구두,
#   검정셔츠-반바지-운동화, 검정셔츠-반바지-구두
# ]

# Example 2:
# Input:
#   tops = [티셔츠]
#   bottoms = [반바지]
#   shoes = [슬리퍼, 샌들]
# Output: [티셔츠-반바지-슬리퍼, 티셔츠-반바지-샌들]

# tops = ["흰셔츠", "검정셔츠"]
# bottoms = ["청바지", "면바지", "반바지"]
# shoes = ["운동화", "구두"]

tops = ["티셔츠"]
bottoms = ["반바지"]
shoes = ["슬리퍼", "샌들"]

result = []
def backtrack(index, combinations):
    if index == 3:
        return result.append(combinations[:])
    
    iterList = tops
    if index == 1:
        iterList = bottoms
    elif index == 2:
        iterList = shoes

    for ele in iterList:
        combinations.append(ele)
        backtrack(index+1, combinations)
        combinations.pop()
    

backtrack(0, [])
print(result)