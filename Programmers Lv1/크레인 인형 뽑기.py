def solution(board, moves):
    s=[0]
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if s[-1] == board[j][i-1]:
                        s.pop()
                        answer += 2
                else:
                    s.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))