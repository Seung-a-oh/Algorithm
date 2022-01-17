N, M = map(int, input().split())
list = list(map(int, input().split()))
l = len(list)
maxlist = []

for _1 in range(0, l-2):
    for _2 in range(_1+1, l-1):
        for _3 in range(_1+2, l):
            sum = list[_1]+list[_2]+list[_3]
            if (sum <= M):
                maxlist.append(sum)

print(max(maxlist))