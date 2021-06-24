temp = 0
n = []
for i in range(4):
    a, b = map(int, input().split())
    temp += (b - a)
    n.append(temp)

print(max(n))