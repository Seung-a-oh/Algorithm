import sys
N = int(sys.stdin.readline().rstrip())

num = 1
count = 1
while(N>num):
    num = num + 6
    count += 1

print(count)

# 시간 초과