import sys

N = int(sys.stdin.readline().rstrip())
all_number = [str(i) for i in range(10**(N-1), 10**N)]
count = 0

if N == 1:
    print(9)
    sys.exit()
    
for num in all_number:
    for n in range(0,N-1):
        if abs(int(num[n])-int(num[n+1])) == 1:
            count += 1
print(count)