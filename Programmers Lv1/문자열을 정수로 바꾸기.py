def solution(s):
    if s[0] == '-':
        answer = int(s[1:])*-1
    else:
        answer = int(s)
    return answer


# 다른 사람의 풀이
# def strToInt(str):
#     a = int(str)
#     return a