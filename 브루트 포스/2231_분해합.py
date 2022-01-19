sN = input()
N = int(sN)

l = len(sN)
m = l * 9
r=0
minlist = []

# for i in range(N-m, N):
for i in range(1, N):
    # print(i)
    for j in str(i):
        r += int(j)

    if int(i)+r == N:
        print(i)        #i가 작은 수 부터 들어가기 때문에 생성자를 찾으면 중단해도 됨.
        break
    r = 0
print(0)