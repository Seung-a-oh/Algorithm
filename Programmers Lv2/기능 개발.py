import math

def solution(progresses, speeds):
    day = [0]*len(progresses)
    answer = []
    
    for i,(x,y) in enumerate(zip(progresses, speeds)):
        day[i] = math.ceil((100-x)/y)
    
    while len(day):
        count = 1
        for j in range(1,len(day)):
            if day[0] >= day[1]:
                count += 1
                day.pop(1)
            else:
                break
        day.pop(0)
        answer.append(count)
    
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speed = [1,1,1,1,1,1]
print(solution(progresses,speed))