def solution(n):
    number = ''
    answer = 0

    while n:
        number = str(n%3) + number
        n //= 3

    for i in range(len(number)):
        answer += int(number[i])*(3**i)
    return answer



# 다른 사람의 풀이
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3
#
#     answer = int(tmp, 3)
#     return answer

print(solution(45))