N = int(input())
array = list(map(int, input().split()))
count = 0

for i in array:
    cnt = 0
    if (i==0):
        continue
    for j in range(2, i+1):
        if (i%j==0):
            cnt += 1
    if (cnt == 1):
        count += 1
print(count)
