M = int(input())
N = int(input())

all = list(range(M,N+1))

for i in range(M,N+1):
    if (i==0):
        continue
    elif i==1:
        all.remove(1)
    for j in range(2, i):
        if (i%j==0):
            all.remove(i)
            break

if len(all) == 0:
    print(-1)
else:
    print(sum(all))
    print(min(all))