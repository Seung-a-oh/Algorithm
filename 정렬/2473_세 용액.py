from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

combi = list(combinations(a,3))
b = abs(sum(combi[0]))
answer = combi[0]

for _ in combi:
    if b > abs(sum(_)):
        b = abs(sum(_))
        answer = list(_)
        
answer.sort()
print(answer[0],answer[1],answer[2])
