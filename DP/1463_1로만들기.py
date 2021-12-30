N = int(input())

# if (N>=1 & N<=10**6):

dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])


# 딕셔너리를 활용한 코드. 시간 단축 가능.
# cache = {1: 0, 2: 1}

# def dp(n):
#     if n in cache:
#         return cache[n]
	
#     # 핵심 코드
#     cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
#     cache[n] = cnt
#     return cnt
    
# print(dp(N))