def solution(numbers, hand):
    answer = ''
    distance = [[4,2],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3],[4,1],[0,0],[4,3]]
    right = 12; left = 10
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        else:
            ld = abs(distance[i][0]-distance[left][0]) + abs(distance[i][1]-distance[left][1])
            rd = abs(distance[i][0]-distance[right][0]) + abs(distance[i][1]-distance[right][1])
            if ld > rd:
                answer += "R"
                right = i
            elif ld < rd:
                answer += "L"
                left = i
            elif ld == rd:
                answer += hand[0].upper()
                if hand == 'right':
                    right = i
                else:
                    left = i
                
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
