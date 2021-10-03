from collections import deque
import sys
read = sys.stdin.readline

m, n, h = map(int, read().split())
g = [[] for i in range(h)]

for i in range(h):
    for j in range(n):
        g[i].append(list(map(int, read().split())))

visited = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]

q = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        x, y, z = q.popleft()
        visited[z][x][y] = 1
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<n and 0<= ny< m and 0<= nz< h and visited[nz][nx][ny]==0 and g[nz][nx][ny]==0:
                q.append([nx, ny, nz])
                visited[nz][nx][ny] = 1
                g[nz][nx][ny] = g[z][x][y] + 1
            
for z in range(h):
    for x in range(n):
        for y in range(m):
            if g[z][x][y] == 1:
                q.append([x, y, z])
bfs()

flag = False
cnt = 0

for z in range(h):
    for x in range(n):
        for y in range(m):
            if g[z][x][y] == 0:
                isTrue = True
            cnt = max(cnt, g[z][x][y])
            
if flag == True:
    print(-1)
else:
    print(cnt - 1)
