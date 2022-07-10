def solution(answers):
    l = len(answers)
    a = [1,2,3,4,5]*((l//5)+1)
    b = [2,1,2,3,2,4,2,5]*((l//8)+1)
    c = [3,3,1,1,2,2,4,4,5,5]*((l//10)+1)
    
    ac = 0; bc = 0; cc = 0;
    for _ in range(l):
        if a[_] == answers[_]:
            ac += 1
        if b[_] == answers[_]:
            bc += 1
        if c[_] == answers[_]:
            cc += 1
    result = {1:ac,2:bc,3:cc}
    answer = [k for k,v in result.items() if max(result.values()) == v]
    max(answer)
    return answer

answer = [1,3,2,4,2]
print(solution(answer))
