N = int(input())

for i in range(N):
    print(" "*(N-i-1),end="")
    print("*"*(i+1))


#추가 공부 코드
# for i in range(N):
#     print(" "*(N-i-1)+"*"*(i+1))

# for i in range(1,N+1):
#     print(" "*(N-i)+"*"*(i))
