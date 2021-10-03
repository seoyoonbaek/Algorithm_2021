import sys
read = sys.stdin.readline

n, m = map(int, read().split())
r, c, d = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]

#북동남서(0123)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
    
def dfs(x, y, d):
    global cnt
    
    #1.청소하기
    if graph[x][y]==0:
        #청소 끝:2
        graph[x][y]=2
        cnt+=1
        
    #2-1.청소할 방향 찾기
    for _ in range(4):
        nd=(d+3)%4
        nx = x+dx[nd]
        ny = y+dy[nd]
        #찾음 -> 재귀
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            dfs(nx, ny, nd)
            return #흠 돌아오는 역할 ?...
        d = nd
    #2-2.모두 되어있 or 벽이면, 후진할 방향=벽x(2) 확인
    nd = (d+2)%4
    nx = x+dx[nd]
    ny = y+dy[nd]
    #벽인 경우(1)
    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
        return
    #후진 가능한 경우(2)
    dfs(nx, ny, d)
    

cnt=0
dfs(r, c, d)
print(cnt)
