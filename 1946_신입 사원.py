import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    score = [0]*N
    for i in range(N):
        score[i] = list(map(int,sys.stdin.readline().split()))
    score.sort()
    min = score[0][1]
    count = 1
    for j in range(1,N):
        if score[j][1] < min:
            min = score[j][1]
            count += 1
    print(count)