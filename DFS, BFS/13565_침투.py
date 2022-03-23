import sys
sys.setrecursionlimit(1000000)

M, N = map(int,sys.stdin.readline().split())

visited = [[0]*(N) for _ in range(M)] 
graph = []

for _ in range(M):
    a = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(a)

def dfs(x,y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return
    if graph[x][y] == 0 and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x+1,y)
        return
 
for i in range(N):
    if graph[0][i] == 0 and visited[0][i] == 0:
        dfs(0,i)

if 1 in visited[M-1]:
    print("YES")
else:
    print("NO")

