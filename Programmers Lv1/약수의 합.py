def solution(n):
    answer = sum(i for i in range(1,n+1) if n%i==0)
    return answer

# 다른 사람의 풀이
# def sumDivisor(num):
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])