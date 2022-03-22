import sys
sys.setrecursionlimit(10000)

N, M = map(int,sys.stdin.readline().split())

visited = [0]*(N+1)
graph = [[0]*(N+1) for _ in range(N+1)] 

def dfs(n):
    visited[n] = 1
    for i in range(1,N+1):
        if visited[i] == 0 and graph[n][i] == 1:
            dfs(i) 

for _ in range(M): 
    a, b = map(int, sys.stdin.readline().split()) 
    graph[a][b] = 1 
    graph[b][a] = 1 

count = 0
for _ in range(1,N+1):
    if visited[_] == 0:
        dfs(_)
        count += 1
        
print(count)
