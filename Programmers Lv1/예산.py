def solution(d, budget):
    d.sort()
    value = 0;  count = 0
    
    for i in range(len(d)):
        if value+d[i] > budget:
            return i
        else:
            value += d[i]
            count = i
    
    return count+1