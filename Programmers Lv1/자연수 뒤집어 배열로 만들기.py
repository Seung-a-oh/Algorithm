def solution(n):
    answer = sorted(list(map(int, list(str(n)))), reverse=True)
    return answer

print(solution(12345))