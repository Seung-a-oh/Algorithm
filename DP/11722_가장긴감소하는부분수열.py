N = int(input())
A = [0]*(N+1)
r = [0]*(N+1)
result = 0

array = input().split()
array = map(int, array)

for j in range(N):
    r[j] = array[j]
    for k in range(j, array):
        if array[k] > array[j]:
            r.append(array[k])
        if len(r) > result:
            result = len(r)

print(result)