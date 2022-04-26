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


n = int(input())

dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            
print(sum(dp[n]) % 1000000000)