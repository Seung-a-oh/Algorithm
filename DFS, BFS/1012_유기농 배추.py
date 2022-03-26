import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return
    elif graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x+1,y)

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())

    visited = [[0]*(M) for _ in range(N)] 
    graph = [[0]*(M) for _ in range(N)]

    for i in range(K): 
        a, b = map(int, sys.stdin.readline().split()) 
        graph[b][a] = 1  

    count = 0
    for x in range(N):
        for y in range(M):
            if visited[x][y] == 0 and graph[x][y] == 1:
                dfs(x,y)
                count += 1
            
    print(count)
