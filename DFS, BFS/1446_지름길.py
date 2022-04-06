import sys

# 지름길의 개수, 고속도로의 길이
N, D = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    # 지름길 시작, 지름길 끝, 지름길 길이
    s, e, w = map(int, sys.stdin.readline().split())

    # 지름길의 도착점이 고속도로의 끝을 넘지 않는 경우에만 지름길 추가
    if e > D:
        continue
    graph.append([s,e,w])

# 자신의 거리가 들은 리스트 생성
distance = [i for i in range(D+1)]

for i in range(D+1):
    # 순수 i까지의 고속도로 거리와 이전까지의 고속도로 길이+1 중 짧은 것 선택
    distance[i] = min(distance[i], distance[i-1]+1)

    for s, e, w in graph:
        # 현재 위치와 지름길의 시작점이 같고, 지름길의 길이가 순수 고속도로 길이보다 짧은 경우
        if i == s and distance[i]+w < distance[e]:
            distance[e] = distance[i] + w
        
print(distance[D])

