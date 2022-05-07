import sys

# 지름길의 개수, 고속도로의 길이
N, D = map(int, sys.stdin.readline().split())

graph = []
distance = [i for i in range(D+1)]

for _ in range(N):
    # 지름길 시작, 지름길 끝, 지름길 길이
    s, e, w = map(int, sys.stdin.readline().split())

    if e > D:
        continue
    graph.append([s,e,w])

for i in range(D+1):
    distance[i] = min(distance[i], distance[i-1]+1)

    for s, e, w in graph:
        if i == s and distance[i]+w < distance[e]:
            distance[e] = distance[i] + w
        
print(distance[D])

