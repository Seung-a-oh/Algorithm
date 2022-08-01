def solution(nums):
    n = len(nums)//2
    num = list(set(nums))
    if len(num) >= n:
        answer = n
    else:
        answer = len(num)
    return answer


# 다른 사람의 코드
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))