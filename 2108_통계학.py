import weakref
from matplotlib.text import get_rotation


N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

print(round(sum(array)/N))
array.sort(); print(array[N//2])
print("최빈값")
print(max(array)-min(array))
