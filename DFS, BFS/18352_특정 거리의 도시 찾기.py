import sys

# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
N, M, K, X = map(int, sys.stdin.readline().split())

visited = [-1] * (N+1)
graph = [[] for _ in range(N+1)]
queue = []

for _ in range(M):
    a,b = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[a].append(b)

def bfs(n):
    queue.append(n)
    visited[n] = 0

    while queue:
        node = queue.pop(0)
        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                queue.append(i)

bfs(X)

for i in range(1, N+1):
    if visited[i] == K:
        print(i)

if K not in visited:
    print(-1)