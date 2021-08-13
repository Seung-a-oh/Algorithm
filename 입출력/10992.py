n = int(input())
for i in range(n):
    if i+1 == n or i == 0:
        print(" "*(n-i-1) + "*"*(2*(i+1)-1))
    else:
        print(" " * (n - i - 1) + "*" + " "*((i-1)*2+1) + "*")