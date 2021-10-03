from collections import deque
import sys
read = sys.stdin.readline

def dfs(v):
    visited_d[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited_d[i]==0 and graph[v][i]==1:
            dfs(i)
    
def bfs(v):
    queue = deque()
    queue.append(v)
    visited_b[v] = 1   
    while queue:
        v = queue.popleft()
        #visited_b[v] =1
        print(v, end=' ')
        for i in range(1, n+1):
            if visited_b[i]==0 and graph[v][i]==1:
                queue.append(i)
                visited_b[i] = 1
                #bfs : queue에 넣는 순간 방문한 것으로 잘 적어주기(pop말고 append!)


n, m, v = map(int, read().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, read().split())
    graph[i][j] = graph[j][i] = 1

visited_d = [0]*(n+1)
visited_b = [0]*(n+1)

dfs(v)
print()
bfs(v)
