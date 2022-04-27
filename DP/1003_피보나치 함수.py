import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [[0,0] for i in range(N+1)]

    if N == 0:
        print("1 0")
        continue
    elif N == 1:
        print("0 1")
        continue
    
    dp[0] = [1,0]
    dp[1] = [0,1]

    for j in range(N+1)[2:]:
        dp[j] = [dp[j-1][k] + dp[j-2][k] for k in range(2)]

    print(dp[N][0], dp[N][1])