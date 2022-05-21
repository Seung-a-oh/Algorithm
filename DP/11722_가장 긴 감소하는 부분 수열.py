import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

dp = [1 for i in range(N)]

# 10 30 10 20 20 10

for i in range(N):
    for j in range(i):
        if li[i] < li[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
