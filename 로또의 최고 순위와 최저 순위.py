def solution(lottos, win_nums):
    min = 0; max = 0
    order = [6,6,5,4,3,2,1]
    
    for i in win_nums:
        if i in lottos:
            min += 1
    for j in lottos:
        if j == 0:
            max += 1
    max += min
    print(min, max)
    answer = [order[min], order[max]]
    return answer

lottos = [44, 1, 0, 0, 31, 25]
wins = [31, 10, 45, 1, 6, 19]
solution(lottos, wins)