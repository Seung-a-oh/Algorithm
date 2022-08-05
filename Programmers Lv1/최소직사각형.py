def solution(sizes):
    w = []
    h = []
    
    for i in sizes:
        i.sort()
    for a,b in sizes:
        w.append(a)
        h.append(b)
    
    answer = max(w)*max(h)
    return answer

# 다른 사람의 풀이
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)
# 둘 중에 큰 것의 최대 값, 둘 중에 작은 것의 최대 값