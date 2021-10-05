#https://fullmoon1344.tistory.com/93
import sys
sys.setrecursionlimit(10000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < N) and (0 <= ny < N):
            #print(5)
            if arr[nx][ny] > h and done[nx][ny] == 0:
                #print(6)
                done[nx][ny] = 1
                dfs(nx, ny, h)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_list=[]

for k in range(max(map(max, arr))):

    # 주어진 배열에서 가장 큰값만큼 반복
    # 매번 초기화
    cnt = 0
    done = [[0]*N for _ in range(N)]
    # 입력 받은 arr배열 탐색
    for i in range(N):

        for j in range(N):
            if arr[i][j] > k and done[i][j] == 0:
                print(3)
                done[i][j] = 1
                cnt += 1
                dfs(i, j, k)
    cnt_list.append(cnt)

print(cnt_list)
