import sys

T = int(sys.stdin.readline())

for _ in range(T):
    zero = 0
    one = 0
    N = int(sys.stdin.readline())
    dp = [[0,0] for i in range(N)]
    if N == 0:
        print("1 0")
        continue
    elif N == 1:
        print("0 1")
        continue
    dp[0] = [1,0]
    dp[1] = [0,1]
    for j in range(len(dp))[2:]:
        dp[j] = [dp[j-1][k] + dp[j-2][k] for k in range(2)]
    print(dp[N-2][0]+dp[N-1][0], dp[N-2][1]+dp[N-1][1])
