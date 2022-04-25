import sys

N = int(sys.stdin.readline().rstrip())
count = 0

if N == 1:
    print(9)
    sys.exit()
    
for num in range(10**(N-1), 10**N):
    s_num = str(num)
    for n in range(0,N-1):
        if abs(int(s_num[n])-int(s_num[n+1])) == 1:
            count += 1
print(count)