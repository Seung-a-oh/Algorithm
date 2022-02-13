N = int(input())

i=1; count = 1

while(N>0):
    N -= i
    i += 1
    count += 1

a=count-1
b=N+count-1

if (a%2==0):
    print(str(1*b)+"/"+str(a-(1*b)+1))
else:
    print(str(a-(1*b)+1)+"/"+str(1*b))
