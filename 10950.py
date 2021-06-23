times = int(input())
list=[]

for i in range(times):
    a=(sum(map(int,input().split())))
    list.append(a)

for i in range(times):
    print(list[i])