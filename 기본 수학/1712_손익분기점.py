import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())

if (b>=c):
    print(-1)
else:
    print(int(a/(c-b)+1))