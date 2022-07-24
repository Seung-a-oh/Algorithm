def solution(s):

    ss = s.lower()
    p = 0; y = 0

    for i in ss:
        if i == 'p':
            p += 1
        elif i == 'y':
            y += 1

    if p == y:
        return True
    else:
        return False

solution('pPoooyY')

# 다른 사람의 코드
# def numPY(s):
#     return s.lower().count('p') == s.lower().count('y')
# -> Count 라이브러리 말고 기본 내장 count가 있음!!