def solution(participant, completion):
    answer = ''
    
    for i in completion:
        participant.remove(i)
    answer = participant[0]

    return answer