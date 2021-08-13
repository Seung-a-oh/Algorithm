n = int(input())
a = 2*n-1

for i in range(a):
    if i < n:
        print(" " * i + "*" * (a-2*i) + " " * i)
    else:
        print(" " * (a-i-1) + "*" * (2*i+2-a) + " " * (a-i-1))
