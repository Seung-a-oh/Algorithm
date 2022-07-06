def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        answer += absolutes[i] if signs[i] else absolutes[i]*(-1)
        
    return answer