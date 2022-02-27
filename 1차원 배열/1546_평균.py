N = int(input())
score = list(map(int, input().split()))
M = max(score)
for _ in range(N):
    score[_] = score[_]/M*100
print(sum(score)/N)