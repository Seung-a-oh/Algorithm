n = int(input())
m = list(map(int, input().split()))
s = sorted(m)

print(s[0], s[-1])
