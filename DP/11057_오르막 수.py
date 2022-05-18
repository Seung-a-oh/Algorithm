import sys

N = int(sys.stdin.readline())

dp = [[0 for i in range(10)] for j in range(N+1)] 

for k in range(10): 
    dp[1][k] = 1 

for n in range(2, N+1): 
    for k in range(10): 
        for sum_k in range(k, 10):
            dp[n][k] += dp[n-1][sum_k] 

print(sum(dp[N]) % 10007)

# 1자리 수 일 때: 0 1 2 3 4 5 6 7 8 9 

# 2자리 수:
# 00 01 02 03 04 05 06 07 08 09
# 11 12 13 14 15 16 17 18 19
# 22 23 24 25 26 27 28 29
# 33 34 35 36 37 38 39 

# 3자리 수:
# 0으로 시작할 때: 2자리수의 모든 수
# 1로 시작할 때: 2자리수에서 0으로 시작하는 수를 뺀 모든 수
# 2로 시작할 때: 2자리수에서 0,1로 시작하는 수를 뺀 모든 수