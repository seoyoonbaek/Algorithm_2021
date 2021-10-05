from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().rstrip())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
ans = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        #벽
        if graph[i][j] == 1:
            ans[i][j] = 1

def bfs(sy, sx):
    q = deque([sy, sx])
    
    visited[i][j] = True
    cnt = 1
    ones = []

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if -1<ny<r and -1<nx<c:
                if visited[ny][nx]: continue
                visited[ny][nx] = True

                if arr[ny][nx] == 0:                  
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    cnt += 1

                else: ones.append((ny, nx))
    
    for y, x in ones:
        visited[y][x] = False
        answer[y][x] += cnt
        if answer[y][x] >= 10: answer[y][x] %= 10

for i in range(n):
    for j in range(m):
        #땅
        if graph[i][j]==0 and visited[i][j]==False:
            bfs(i,j)

for i in range(r):
    print(''.join(map(str,answer[i])))
