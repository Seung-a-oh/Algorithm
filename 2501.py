n, k, answer = *map(int, input().split()), 0
for i in range(1, n + 1):
    if not (n % i):
        k -= 1
        if not k:
            answer = i
            break
print(answer)