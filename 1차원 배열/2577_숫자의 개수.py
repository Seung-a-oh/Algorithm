a=int(input())
b=int(input())
c=int(input())
n = str(a*b*c)

array = [0]*10

for i in n:
    array[int(i)] += 1

for j in array:
    print(j)