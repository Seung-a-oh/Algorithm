# 첫번째 풀이 - 효율성 실패
# def solution(arr):
#     answer = []
#     p = arr[0]
    
#     for i in range(1,len(arr)):
#         if p != arr[i]:
#             answer.append(p)
#             p = arr[i]

#     if answer[-1] != p:
#         answer.append(p)

#     return answer

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])

    return answer


print(solution([1,1,3,3,0,1,1]))