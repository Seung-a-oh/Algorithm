# T = int(input())

# def cal(n,k):
#     people = 0

#     if n == 0:
#         return k
#     else:
#         for i in range(k):
#             people += cal(n-1,i+1)
#     return people

# for _ in range(T):
#     n = int(input())
#     k = int(input())

#     print(cal(n,k))

# -> 시간 초과
# ---------------------------------------------------

T = int(input())

for _ in range(T):
    n = int(input())
    k = int(input())

    people = [p+1 for p in range(k)]
    people.reverse()

    for j in range(n):
        for i in range(k):
            people[i] = sum(people[i:])

    print(people[0])
