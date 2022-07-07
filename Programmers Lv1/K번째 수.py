def solution(array, commands):
    answer = []
    for i in commands:
        li = array[i[0]-1:i[1]]
        li.sort()
        answer.append(li[i[2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

# 다른 사람의 코드
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer