# N = int(input())
# # a = [0]*(N+1)
# r = [0]
# result = 0

# a = input().split()
# a = [int(_) for _ in a]

# for j in range(N):
#     r[0] = a[j]
#     for k in range(j+1, N):
#         if r[len(r)-1] > a[k]:
#             r.append(a[k])
#             print(len(r))
#     if len(r) > result:
#         result = len(r)
#     print(r)
#     r=[0]
    
# print(result)

N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if numbers[j] > numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))