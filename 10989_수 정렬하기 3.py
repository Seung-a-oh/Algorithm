import sys

N = int(sys.stdin.readline())
li = [0]*10001

for i in range(N):
    a = int(sys.stdin.readline())
    li[a] += li[a] + 1

for j in range(10001):
    if li[j] != 0:
        for k in range(li[i]):
            print(i+1)