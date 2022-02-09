import sys
import math

a,b,v = map(int, sys.stdin.readline().rstrip().split())

print(math.ceil((v-a)/(a-b)+1))
# print(1-(v-a)//(b-a))
