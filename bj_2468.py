#왜 틀린거지,,,?

import sys
read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]  #왜 될떄도 안될떄도?

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, p):
    visited[x][y]=1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<n and 0<=ny<n:
#            print(5)
            if graph[nx][ny]>=p and visited[nx][ny]==0:
                #print(6)
                dfs(nx, ny, p)
        
    
cnt_list = []
for p in range(1, max(map(max, graph))+1):  #!
    print(1)
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    
    for i in range(n):

        for j in range(n):
            if graph[i][j]>=p and visited[i][j]==0:
                print(3)
                dfs(0, 0, p)
                cnt+=1
    
    cnt_list.append(cnt)

print(cnt_list)

#https://fullmoon1344.tistory.com/93
