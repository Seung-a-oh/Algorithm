import sys
sys.setrecursionlimit(10000)

# 세로 길이, 가로 길이, 개수
N, M, K = map(int, sys.stdin.readline().split())

graph = [[0]*(M+1) for _ in range(N+1)]
visited = [[0]*(M+1) for _ in range(N+1)]

count = 0
large = []
def dfs(x,y):
    global count
    if x <= 0 or x >= N+1 or y <= 0 or y >= M+1:
        return
    elif graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        count += 1
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x+1,y)
    large.append(count)


for _ in range(K):
    # 행, 열 (1,1)~
    r,c = map(int,sys.stdin.readline().split())
    graph[r][c] = 1

for x in range(N+1):
    for y in range(M+1):
        if visited[x][y] == 0 and graph[x][y] == 1:
            count = 0
            dfs(x,y)
print(max(large))