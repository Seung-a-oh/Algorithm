def solution(n, lost, reserve):
    l = list(set(lost) - set(reserve))
    r = list(set(reserve) - set(lost))
    
    answer = n-len(l)
    
    for i in range(len(r)):
        if r[i]-1 in l:
            answer += 1
            l.remove(r[i]-1)
        elif r[i]+1 in l:
            answer += 1
            l.remove(r[i]+1)

    return answer

solution(5,[2, 4],[1, 3, 5])