#idle에서는 돌아가는데 runtime error 발생

from sys import stdin
read = stdin.readline

n, m = map(int, read().split())
g = [[int(x) for x in input().split()] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#1년 후, recount (따로 list 만들어서 빼줘야 함, 전 줄이 반영되어버림)
def melt(g):
    del_g = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j]>0:
                del_cnt=0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<m and g[nx][ny]==0:
                        del_cnt+=1
                del_g[i][j]=del_cnt
    for i in range(n):
        for j in range(m):
            g[i][j]-=del_g[i][j]
    return g

#덩어리 몇 개인지 체크
def dfs(x, y, visited):

    visited[x][y]=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if g[nx][ny]>0 and visited[nx][ny]==0:
                dfs(nx, ny, visited)
    return 1

year_cnt = 0

while True:
    #덩어리 체크
    ice_cnt=0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j]>0 and visited[i][j]==0:  #체크(덩어리 체크 시작할까?)
                ice_cnt += dfs(i, j, visited)

    if ice_cnt==0:
        year_cnt=0
        break
    if ice_cnt>=2:
        break
    
    #1년 후(녹이기)
    g = melt(g)
    year_cnt += 1   

print(year_cnt)



