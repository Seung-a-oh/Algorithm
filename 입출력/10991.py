n = int(input())

for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(1, i+1):
        print("*",end=' ')
    print()

#추가 공부 코드
# n = input()
# n = int(n)
# for i in range(n):
#     print(" " * (n - i - 1) + "* " * (i + 1))