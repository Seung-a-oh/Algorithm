def solution(price, money, count):
    answer = sum([price*i for i in range(1,count+1)])-money
    if answer <= 0:
        answer = 0
    return answer

# 다른 사람의 풀이
# def solution(price, money, count):
#     return max(0,price*(count+1)*count//2-money)
