N = int(input())
stair=[0]*(N+1)

for i in range(1,N+1):
    stair[i] = int(input())

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2] 

    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])  

print(dp[N])