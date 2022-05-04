import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = sys.stdin.readline()

sum = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            sum += dial.index(i)+3
print(sum)
