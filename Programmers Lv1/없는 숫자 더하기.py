def solution(numbers):
    answer = 0
    
    for _ in range(10):
        if _ not in numbers:
            answer += _
    
    return answer


# 다른 사람의 풀이
# def solution(numbers):  
#     return 45 - sum(numbers)