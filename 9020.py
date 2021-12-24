T = int(input())
N = []
r = []
mini = []

def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True

def minimum():
    for l in r:
        a,b = l.split(" ")
        mini.append(abs(int(a)-int(b)))
    return mini.index(min(mini))

for i in range(T):
    N.append(int(input()))

for j in N:
    for k in range(j//2):
        if ((prime(k) == True) & (prime(j-k) == True)):
            r.append(str(k)+" "+str(j-k))
    print(r[minimum()])
    mini.clear()
    r.clear()
