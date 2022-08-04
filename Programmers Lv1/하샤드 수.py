def solution(x):
    s = 0
    for i in str(x):
        s += int(i)
    answer = True if x%s==0 else False
    return answer

# 다른 사람의 풀이
# def Harshad(n):
#     return n % sum([int(c) for c in str(n)]) == 0