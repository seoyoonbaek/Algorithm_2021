#예제 4 실패

from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = []

for i in range(n):
    graph.append(list(read()))
    
#visited = [[0]*m for _ in range(n)] -> 필요없

#배열을 int형으로 선언
graph[0][0] = 1

q = deque()
q.append([0, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        #공간 벗어나지 않는 경우
        if 0<=nx<n and 0<=ny<m:
            if nx==n and ny==m:
                break
            elif graph[nx][ny]=="1" or graph[nx][ny]==1:
                q.append([nx, ny])
                graph[nx][ny] = int(graph[x][y]) +1
                print(nx, ny, graph[nx][ny])
            
print(graph[nx][ny])




    
