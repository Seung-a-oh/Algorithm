sN = input()
N = int(sN)

l = len(sN)
m = l * 9
r=0
minlist = []

for i in range(N-m, N):
    for j in str(i):
        r += int(j)

    if int(i)+r == N:
        minlist.append(i)
    r = 0

print(min(minlist))