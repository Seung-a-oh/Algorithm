def solution():
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]

# 다른 사람의 풀이
# def solution(n):
#     num = ['1','2','4']
# answer = ""

# while n > 0:
#     n -= 1
#     answer = num[n % 3] + answer
#     n //= 3

# return answer