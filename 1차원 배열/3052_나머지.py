a = []
rest = [0]*1000

for _ in range(10):
    a.append(int(input()))

for _ in a:
    rest[_%42] = 1

print(sum(rest))