import sys

T = int(sys.stdin.readline())

def fibonacci(n):
    global zero
    global one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for _ in range(T):
    zero = 0
    one = 0
    N = int(sys.stdin.readline())
    fibonacci(N)
    print(zero, one)