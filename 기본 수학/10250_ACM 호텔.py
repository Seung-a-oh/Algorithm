T = int(input())

for _ in range(T):
    # 층, 호, 손님 순서
    H, W, N = map(int, input().split())
    if (N%H==0):
        floor = H
        room = N // H
    else:
        floor = N % H
        room = N // H + 1

    print(floor*100+room)
