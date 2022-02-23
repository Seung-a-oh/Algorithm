# -----------------시간 초과-------------------
# def Prime(num):
#     if num == 1:
#         return 1
#     else:
#         for n in range(2, int(num**0.5)+1):
#             if num % n == 0:
#                 return 0
#         return 1

# while True:
#     N = int(input())
#     if N == 0: break

#     count = 0
#     for i in range(N+1, 2*N+1):
#         count += Prime(i)
#     print(count)
# -------------------------------------------
        
# -----------------또 시간 초과---------------
# while True:
#     N = int(input())
#     if N == 0: break
    
#     count = 0
#     for i in range(N+1, 2*N+1):
#         for n in range(2, int(i**0.5)+1):
#             if i % n == 0:
#                 break
#         count += 1
#     print(count)
# ------------------------------------------

k = 123456*2+1
all = [1]*k

for i in range(2,k):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            all[i] = 0
            break
while True:
    N = int(input())
    if N == 0: break
    
    count = 0; sum = 0
    
    for i in range(N+1, 2*N+1):
        sum += all[i]
    print(sum)