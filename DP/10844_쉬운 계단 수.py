# import sys

# N = int(sys.stdin.readline().rstrip())
# count = 0

# if N == 1:
#     print(9)
#     sys.exit()
    
# for num in range(10**(N-1), 10**N):
#     s_num = str(num)
#     for n in range(0,N-1):
#         if abs(int(s_num[n])-int(s_num[n+1])) == 1:
#             count += 1
# print(count)

import sys

N = int(sys.stdin.readline())

dp = [[0 for i in range(10)] for j in range(101)]

for k in range(1, 10):
    dp[1][k] = 1

for n in range(2, N + 1):
    for k in range(10):
        if k == 0:
            dp[n][k] = dp[n-1][1]
        elif k == 9:
            dp[n][k] = dp[n-1][8]
        else:
            dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]

print(sum(dp[n]) % 1000000000)