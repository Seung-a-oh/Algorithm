def solution(s, n):
    answer = ""
    asc = [ord(i)+n for i in s]
    for _ in asc:
        print(_)
        if _-n != 32:
            if chr(_-n).islower():
                if _ > 122:
                    answer += chr(_-26)
                else:
                    answer += chr(_)
            else:
                if _ > 90:
                    answer += chr(_-26)
                else:
                    answer += chr(_)
        else:
            answer += " "
    return answer

print(solution("a B z", 4))



# 다른 사람의 코드
# def solution(s, n):
#     answer = ''
#     for i in s:
#         if i:
#             if i >= 'A' and i <= 'Z':
#                 answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
#             elif i >= 'a' and i <= 'z':
#                 answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
#             else : answer += ' '
#     return answer