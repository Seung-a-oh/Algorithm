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
        

while True:
    N = int(input())
    if N == 0: break
    
    count = 0
    for i in range(N+1, 2*N+1):
        a=True
        for n in range(2, int(i**0.5)+1):
            if N % n == 0:
                a=False
        if a:
            count += 1
    print(count)
        