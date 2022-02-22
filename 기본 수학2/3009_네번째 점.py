a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

if a1==b1:
    x = c1
elif a1==c1:
    x = b1
elif b1==c1:
    x = a1

if a2==b2:
    y = c2
elif a2==c2:
    y = b2
elif b2==c2:
    y = a2

print(x ,y)