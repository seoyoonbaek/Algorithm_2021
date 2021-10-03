#dfs
from sys import stdin
read = stdin.readline

n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
#graph2 = [[]]*(n+1) <- 왜 이게 아니지?..

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0]*(n+1)

def dfs(v):
    global cnt
    visited[v] = 1
    cnt+=1
    for i in graph[v]:
        if visited[i] ==0:
            dfs(i)


dfs(1)
print(cnt-1)
    
