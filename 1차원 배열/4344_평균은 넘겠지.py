T = int(input())
for _ in range(T):
    a = list(map(int, input().split(" ")))
    n = a[0];    a = a[1:]
    count = 0
    avg = sum(a)/len(a)
    for i in a:
        if i > avg:
            count += 1
    print(f'{count/n*100:.3f}%')
    # -> 0.000을 출력하기 위해선 round가 아닌 format을 써야한다.