# f = list(range(10))

# def fib(i):
#     if(f[i]!=0):
#         return f[i]
#     else:
#         if (i==1 | i==2):
#             f[i]=1
#         else:
#             f[i] = f[i-1]+f[i-2]
#         return f[i]



# f = []*(n+1)
# f[0] = 0
# f[1] = 1

# for i in range(n-1):
#     f[i+2] = f[i] + f[i+1]

# print(f[n])

# 맞음
# n = int(input())
# one,two, three = 0, 1, 2
# for i in range(n):
#     three = one + two
#     one = two
#     two = three
# print(one)

#맞음
# n = int(input())
# one,two,three = 0, 1, 0
# for i in range(n):
#     three = one
#     one = two
#     two = three + one

# print(two)

#틀림
n = int(input())
one,two, three = 0, 1, 2
for i in range(n-1):
    three = one + two
    one = two
    two = three
print(three)


# N = int(input())
# F0, F1 = 0, 1
# for i in range(N):
#     F0, F1 = F1, F0+F1
#     print(F0)

# print(F0)


# n = int(input())
# f = 0
# s = 1
# tmp = 0
# for i in range(n):
#     tmp = f
#     f = s
#     s = tmp + s
# print(f)