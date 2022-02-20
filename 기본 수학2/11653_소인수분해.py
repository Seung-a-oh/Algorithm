n = N = int(input())

num = []
i=2
while i<=N:
    if n % i == 0:
        n = n//i
        print(i)
    else:
        i += 1    
