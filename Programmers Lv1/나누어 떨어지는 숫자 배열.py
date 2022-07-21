def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if not i % divisor:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer

# 다른 사람의 풀이
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
