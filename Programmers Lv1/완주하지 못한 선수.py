from collections import Counter

def solution(participant, completion):
    answer = ''

    p = Counter(participant)
    c = Counter(completion)
    a = p-c
    answer = [k for k,v in a.items() if v == 1][0]

    return answer

p = ["mislav", "stanko", "mislav", "ana"]
c = ["mislav", "stanko", "ana"]
print(solution(p,c))


# 다른 사람의 코드
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]