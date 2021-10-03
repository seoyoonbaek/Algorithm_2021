from sys import stdin
read = stdin.readline

def dfs(x, y, cnt):
    visited[x][y]=1
    cnt+=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==1 and visited[nx][ny]==0:
                cnt = dfs(nx, ny, cnt)  #return 할당 잊지마
    return cnt


n = int(read())
graph = []
visited = [[0]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, read().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result_list=[]
       
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0: #체
            h_cnt = dfs(i, j, 0)
            result_list.append(h_cnt)
print(len(result_list))
for h in sorted(result_list):
    print(h)
        
