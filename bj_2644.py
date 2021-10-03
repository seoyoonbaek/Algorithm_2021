from collections import deque
import sys

read = sys.stdin.readline

n = int(read())
a, b = map(int, read().split())
m = int(read())

g = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

visited = [0 for i in range(n+1)]

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    
    while q:
        v = q.popleft()
        for i in g[v]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = result[v] + 1
                q.append(i)

                
result = [0 for i in range(n + 1)]
bfs(a)
print(result[b] if result[b] != 0 else -1)
