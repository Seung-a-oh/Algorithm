def solution(a, b):
    if a-b >= 0:
        l = [i for i in range(b,a+1)]
    else:
        l = [i for i in range(a, b+1)]
    answer = sum(l)
    return answer